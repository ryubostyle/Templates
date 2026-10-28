import os
from datetime import datetime
import yaml

class RecyclingProcessor:
    """
    【分別・鎮火・焼却・昇華・零点】の理を静かに宿す、無駄なき全自動プラント
    """
    
    TEXT_EXTS = ('.txt', '.md', '.html', '.json', '.yaml', '.yml', '.csv')

    def __init__(self, trushes_dir: str, archives_dir: str):
        self.trushes_dir = trushes_dir
        self.archives_dir = archives_dir

    def sweep_and_transform(self) -> str:
        os.makedirs(self.trushes_dir, exist_ok=True)
        os.makedirs(self.archives_dir, exist_ok=True)
        
        # ① 回収：隠しファイル（.gitkeep等）を除いた最も古き断片を迎える
        raws = [f for f in os.listdir(self.trushes_dir) if not f.startswith('.') and os.path.isfile(os.path.join(self.trushes_dir, f))]
        if not raws:
            return self._zen_void()
        
        target = sorted(raws)[0]
        path = os.path.join(self.trushes_dir, target)
        
        # ② 分別：素材の適格性を静かに見極める
        ok, payload = self._inspect(path, target)
        
        # ③ 鎮火 or ④ 焼却
        return self._quarantine(path, target, payload) if not ok else self._harmonize(path, target, payload)

    def _inspect(self, path: str, name: str):
        if not name.lower().endswith(self.TEXT_EXTS):
            return False, f"非テキスト系の異物を検知: {name}"
        try:
            with open(path, "r", encoding="utf-8") as f:
                return True, f.read()
        except Exception as e:
            return False, f"デコードの破綻を検知: {e}"

    def _harmonize(self, path: str, name: str, content: str) -> str:
        os.remove(path)
        return self._stamp("scroll", "混沌からの昇華", name, {"type": "recycled_draft", "content": content.strip()}, True)

    def _quarantine(self, path: str, name: str, reason: str) -> str:
        os.remove(path)
        return self._stamp("quarantine", "検疫と鎮火の記録", name, {"type": "quarantined_fragment", "reason": reason}, False)

    def _zen_void(self) -> str:
        return self._stamp("void", "静寂の記録", "void", {"type": "void_echo", "content": "trushes/ は静寂に包まれている。"}, True)

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
            "latent_questions": ["この静けさや異物の中に、次なる秩序の芽生えはあるか？"],
            "provenance": {
                "source_preserved": preserved,
                "interpretation_status": f"{prefix}_harmonized",
                "generated_by": "core.RecyclingProcessor"
            }
        }
        
        with open(filepath, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)
            
        print(f"✨ [RecyclingProcessor] 地層へ静かに定着: {filepath}")
        return filepath
