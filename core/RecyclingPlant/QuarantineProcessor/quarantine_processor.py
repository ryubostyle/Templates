import os
from core.RecyclingPlant.recycling_processor import RecyclingProcessor

class QuarantineProcessor(RecyclingProcessor):
    def __init__(self, parent_trushes: str, archives_dir: str):
        super().__init__(parent_trushes, archives_dir)
        self.local_trushes = os.path.join(os.path.dirname(__file__), "trushes")
        os.makedirs(self.local_trushes, exist_ok=True)

    def process_cascade(self) -> str:
        self._generate_index_md(self.local_trushes, "Quarantine Trash Box (検疫ゴミ箱)")
        
        # 上流（root_trushes）から素材を回収
        raws = [f for f in os.listdir(self.root_trushes_dir) if not f.startswith('.') and os.path.isfile(os.path.join(self.root_trushes_dir, f))]
        if not raws:
            return None

        # ここでは「テキストでもメディアでもない完全な未定義ファイル」を検疫対象とする例
        # あるいはすべての入り口として一旦ここで受け止めることも可能
        target = sorted(raws)[0]
        src_path = os.path.join(self.root_trushes_dir, target)
        
        text_exts = ('.txt', '.md', '.html', '.json', '.yaml', '.yml', '.csv')
        image_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
        media_exts = ('.mp3', '.mp4', '.wav', '.pdf', '.psd')

        lower_name = target.lower()
        if lower_name.endswith(text_exts + image_exts + media_exts):
            # 既知のファイルであれば、ここでは処理せず下流（TextやMedia）へ譲る
            return None

        # ── 未定義の異物の場合 ──
        dest_path = os.path.join(self.local_trushes, target)
        os.rename(src_path, dest_path) # 上流から自分の trushes/ へ移動
        
        print(f"🛡️ [QuarantineProcessor] 未定義の異物を検疫し、専属 trushes/ へ隔離しました: {target}")
        
        meta = {
            "type": "quarantined_fragment",
            "reason": f"未定義の異物のため、QuarantineProcessorのゴミ箱へ隔離: {target}"
        }
        return self._stamp("quarantine", "検疫と鎮火の記録", target, meta, True)
