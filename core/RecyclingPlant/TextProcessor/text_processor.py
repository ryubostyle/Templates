import os
from core.RecyclingPlant.recycling_processor import RecyclingProcessor

class TextRecyclingProcessor(RecyclingProcessor):
    TEXT_EXTS = ('.txt', '.md', '.html', '.json', '.yaml', '.yml', '.csv')

    def __init__(self, parent_trushes: str, archives_dir: str):
        super().__init__(parent_trushes, archives_dir)
        self.local_trushes = os.path.join(os.path.dirname(__file__), "trushes")
        os.makedirs(self.local_trushes, exist_ok=True)

    def process_cascade(self) -> str:
        self._generate_index_md(self.local_trushes, "Text Trash Box (文書ゴミ箱)")
        
        raws = [f for f in os.listdir(self.root_trushes_dir) if not f.startswith('.') and os.path.isfile(os.path.join(self.root_trushes_dir, f))]
        if not raws:
            return None

        target = sorted(raws)[0]
        src_path = os.path.join(self.root_trushes_dir, target)

        if not target.lower().endswith(self.TEXT_EXTS):
            return None # テキストでなければ下流（Media）へ譲る

        try:
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
            os.remove(src_path) # 焼却・昇華完了
            print(f"✨ [TextRecyclingProcessor] 文書を炉で美しく昇華しました: {target}")
            return self._stamp("scroll", "混沌からの昇華（テキスト）", target, {"type": "recycled_draft", "content": content.strip()}, True)
        except Exception as e:
            # デコード破綻等は自身の trushes/ へ逃がす
            dest_path = os.path.join(self.local_trushes, target)
            os.rename(src_path, dest_path)
            return self._stamp("quarantine", "テキストデコード破綻の記録", target, {"reason": str(e)}, True)
