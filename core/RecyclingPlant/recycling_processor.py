import os
from datetime import datetime
import yaml

class RecyclingProcessor:
    """
    【回収と零点】の骨組みだけを司る、静寂の基底プロセッサ
    """
    def __init__(self, trushes_dir: str, archives_dir: str):
        self.trushes_dir = trushes_dir
        self.archives_dir = archives_dir

    def sweep_and_transform(self) -> str:
        os.makedirs(self.trushes_dir, exist_ok=True)
        os.makedirs(self.archives_dir, exist_ok=True)
        
        raws = [f for f in os.listdir(self.trushes_dir) if not f.startswith('.') and os.path.isfile(os.path.join(self.trushes_dir, f))]
        if not raws:
            return self._zen_void()
        
        target = sorted(raws)[0]
        path = os.path.join(self.trushes_dir, target)
        
        # 素材の適格性に応じて、適切な子クラス（プロセッサ）へ委譲する
        return self._dispatch_processor(path, target)

    def _dispatch_processor(self, path: str, name: str) -> str:
        # ここで素材を見極め、適切な子クラスのインスタンスを生成・実行する
        # （※実装例として、テキストかメディアかを判定して委譲）
        from core.text_processor import TextRecyclingProcessor
        from core.media_processor import MediaRecyclingProcessor
        
        if TextRecyclingProcessor.can_process(name, path):
            return TextRecyclingProcessor(self.trushes_dir, self.archives_dir).process(path, name)
        else:
            return MediaRecyclingProcessor(self.trushes_dir, self.archives_dir).process(path, name)

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
            "latent_questions": ["それぞれの断片が持つ理は、システムにどのような進化をもたらすか？"],
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
