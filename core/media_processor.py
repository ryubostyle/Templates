from core.recycling_processor import RecyclingProcessor
import os

class MediaRecyclingProcessor(RecyclingProcessor):
    @classmethod
    def can_process(cls, name: str, path: str) -> bool:
        # メディアやその他の異物判定
        return True

    def process(self, path: str, name: str) -> str:
        file_size = os.path.getsize(path)
        lower_name = name.lower()
        
        if lower_name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
            meta = {"type": "visual_fragment", "filename": name, "file_size_bytes": file_size, "description": "視覚の断片（画像）が投下された。"}
            prefix = "multimedia"
            title = "混沌からの昇華（メディア）"
        elif lower_name.endswith(('.mp3', '.mp4', '.wav', '.pdf', '.psd')):
            meta = {"type": "audio_or_doc_fragment", "filename": name, "file_size_bytes": file_size, "description": "音声・動画・ドキュメントの断片が投された。"}
            prefix = "multimedia"
            title = "混沌からの昇華（メディア）"
        else:
            meta = {"type": "quarantined_fragment", "reason": f"未定義の異物を検知: {name}"}
            prefix = "quarantine"
            title = "検疫と鎮火の記録"

        os.remove(path)
        return self._stamp(prefix, title, name, meta, True if prefix == "multimedia" else False)
