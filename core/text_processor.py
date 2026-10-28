from core.recycling_processor import RecyclingProcessor
import os

class TextRecyclingProcessor(RecyclingProcessor):
    TEXT_EXTS = ('.txt', '.md', '.html', '.json', '.yaml', '.yml', '.csv')

    @classmethod
    def can_process(cls, name: str, path: str) -> bool:
        if not name.lower().endswith(cls.TEXT_EXTS):
            return False
        try:
            with open(path, "r", encoding="utf-8") as f:
                f.read()
            return True
        except:
            return False

    def process(self, path: str, name: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        os.remove(path)
        return self._stamp("scroll", "混沌からの昇華（テキスト）", name, {"type": "recycled_draft", "content": content.strip()}, True)
