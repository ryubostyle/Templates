import os
from core.RecyclingPlant.recycling_processor import RecyclingProcessor

class MediaRecyclingProcessor(RecyclingProcessor):
    IMAGE_EXTS = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    MEDIA_EXTS = ('.mp3', '.mp4', '.wav', '.pdf', '.psd')

    def __init__(self, parent_trushes: str, archives_dir: str):
        super().__init__(parent_trushes, archives_dir)
        self.local_trushes = os.path.join(os.path.dirname(__file__), "trushes")
        os.makedirs(self.local_trushes, exist_ok=True)

    def process_cascade(self) -> str:
        self._generate_index_md(self.local_trushes, "Media Trash Box (メディアゴミ箱)")
        
        raws = [f for f in os.listdir(self.root_trushes_dir) if not f.startswith('.') and os.path.isfile(os.path.join(self.root_trushes_dir, f))]
        if not raws:
            return None

        target = sorted(raws)[0]
        src_path = os.path.join(self.root_trushes_dir, target)

        if not target.lower().endswith(self.IMAGE_EXTS + self.MEDIA_EXTS):
            # ここまで来ても処理できない場合は自身の trushes/（ゴミ箱）に残す
            dest_path = os.path.join(self.local_trushes, target)
            os.rename(src_path, dest_path)
            print(f"🧯 [MediaRecyclingProcessor] 処理不能な断片を自身のゴミ箱へ残置: {target}")
            return self._stamp("quarantine", "未解決断片の記録", target, {"reason": "どの炉でも処理できませんでした"}, True)

        file_size = os.path.getsize(src_path)
        os.remove(src_path) # メディア昇華完了
        
        meta = {
            "type": "visual_or_audio_fragment",
            "filename": target,
            "file_size_bytes": file_size,
            "description": "マルチメディアの断片が美しくネガ化された。"
        }
        print(f"✨ [MediaRecyclingProcessor] メディアをネガフィルムへ定着: {target}")
        return self._stamp("multimedia", "混沌からの昇華（メディア）", target, meta, True)
