import os
from datetime import datetime
import yaml

class RecyclingProcessor:
    """
    【回収・零点・index自動生成】を司る静寂の基底プロセッサ
    """
    def __init__(self, root_trushes_dir: str, archives_dir: str):
        self.root_trushes_dir = root_trushes_dir
        self.archives_dir = archives_dir

    def sweep_and_transform(self) -> str:
        os.makedirs(self.root_trushes_dir, exist_ok=True)
        os.makedirs(self.archives_dir, exist_ok=True)
        
        # 零点（index.md）の自動生成
        self._generate_index_md(self.root_trushes_dir, "大元のゴミ捨て場（Root Trushes）")

        # 1. 各専門プロセッサを順次起動し、多段式パイプラインを巡回する
        from core.RecyclingPlant.QuarantineProcessor.quarantine_processor import QuarantineProcessor
        from core.RecyclingPlant.TextProcessor.text_processor import TextRecyclingProcessor
        from core.RecyclingPlant.MediaProcessor.media_processor import MediaRecyclingProcessor

        # 順序: quarantine(未定義検疫) -> text(文書昇華) -> media(メディア昇華)
        processors = [
            QuarantineProcessor(self.root_trushes_dir, self.archives_dir),
            TextRecyclingProcessor(self.root_trushes_dir, self.archives_dir),
            MediaRecyclingProcessor(self.root_trushes_dir, self.archives_dir)
        ]

        result_film = None
        for proc in processors:
            result_film = proc.process_cascade()
            if result_film:
                break # いずれかの棟で処理（または検疫）が行われたらその幕とする

        if not result_film:
            return self._zen_void()

        return result_film

    def _zen_void(self) -> str:
        return self._stamp("void", "静寂の記録", "void", {"type": "void_echo", "content": "すべての trushes/ は静寂に包まれている。"}, True)

    def _stamp(self, prefix: str, title_base: str, origin: str, source_meta: dict, preserved: bool) -> str:
        today = datetime.now().strftime("%Y.%m.%d")
        count = sum(1 for f in os.listdir(self.archives_dir) if f.startswith(f"{today}.") and f.endswith(".film.yaml"))
        seq = f"{count + 1:02d}"
        
        filepath = os.path.join(self.archives_dir, f"{today}.{seq}.film.yaml")
        source_meta["origin_file"] = origin
        
        data = {
            "film_id": f"{prefix}-{today}-{seq}",
            "title": f"{title_base} ── {today} 第{seq}幕",
            "source": source_meta,
            "latent_questions": ["多段式プラントを巡る断片は、庵にどのような秩序をもたらすか？"],
            "provenance": {
                "source_preserved": preserved,
                "interpretation_status": f"{prefix}_harmonized",
                "generated_by": "core.RecyclingPlant.RecyclingProcessor"
            }
        }
        
        with open(filepath, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)
            
        print(f"✨ [RecyclingProcessor] 地層へ静かに定着: {filepath}")
        return filepath

    def _generate_index_md(self, target_dir: str, title: str):
        """どの階層のフォルダーにアクセスしても零点（index.md）として美しく表示させる"""
        os.makedirs(target_dir, exist_ok=True)
        index_path = os.path.join(target_dir, "index.md")
        files = [f for f in os.listdir(target_dir) if not f.startswith('.')]
        
        content = f"# {title}\n\n> 零点 ── 現在のこの空間に漂う断片たち\n\n"
        content += "### 📁 収納されている断片\n"
        if files:
            for f in files:
                content += f"- {f}\n"
        else:
            content += "- *(静寂：断片はありません)*\n"
            
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)
