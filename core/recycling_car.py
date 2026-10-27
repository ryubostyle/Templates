import os
from datetime import datetime
import yaml

class RecyclingCar:
    """trushes/ のカオスを回収し、命名規則に従ってフィルム（YAML）へ昇華させる親クラス"""
    
    def __init__(self, trushes_dir: str, archives_dir: str):
        self.trushes_dir = trushes_dir
        self.archives_dir = archives_dir

    def sweep_and_transform(self) -> str:
        """ゴミ捨て場を巡回し、未処理のドラフトを回収して新しいfilm.yamlを製版する"""
        os.makedirs(self.trushes_dir, exist_ok=True)
        os.makedirs(self.archives_dir, exist_ok=True)
        
        # trushes/ 内のファイル一覧を取得
        draft_files = [f for f in os.listdir(self.trushes_dir) if os.path.isfile(os.path.join(self.trushes_dir, f))]
        
        if not draft_files:
            # 回収すべきカオスがない場合は、デフォルトの思考の断片を生成
            raw_content = "trushes/ は静寂に包まれている。新たなカオスの投下を待っている状態。"
            source_name = "void_echo"
        else:
            # 最も古い（あるいは最初の）ドラフトを回収対象とする
            target_draft = sorted(draft_files)[0]
            draft_path = os.path.join(self.trushes_dir, target_draft)
            
            with open(draft_path, "r", encoding="utf-8") as f:
                raw_content = f.read()
            source_name = target_draft
            
            # 役目を終えたドラフトは綺麗に回収（削除、または退避）
            os.remove(draft_path)
            print(f"🧹 [RecyclingCar] カオスを回収しました: {draft_path}")

        # yyyy.mm.dd.nn.film.yaml の命名規則を適用
        today_str = datetime.now().strftime("%Y.%m.%d")
        existing_archives = os.listdir(self.archives_dir)
        today_prefix = f"{today_str}."
        today_count = sum(1 for f in existing_archives if f.startswith(today_prefix) and f.endswith(".film.yaml"))
        sequence_number = f"{today_count + 1:02d}"
        
        new_film_filename = f"{today_str}.{sequence_number}.film.yaml"
        new_film_path = os.path.join(self.archives_dir, new_film_filename)
        
        # フィルムデータの構築
        film_data = {
            "film_id": f"scroll-{today_str}-{sequence_number}",
            "title": f"混沌からの昇華 ── {today_str} 第{sequence_number}幕",
            "source": {
                "type": "recycled_draft",
                "origin_file": source_name,
                "content": raw_content.strip()
            },
            "latent_questions": [
                "ゴミ捨て場（trushes）から回収された断片は、スクリーンに何を映し出すか？",
                "混沌を秩序へと変えるこの循環は、システムにどのような進化をもたらすか？"
            ],
            "provenance": {
                "source_preserved": True,
                "interpretation_status": "recycled_and_harmonized",
                "generated_by": "core.RecyclingCar"
            }
        }
        
        # ネガフィルムの定着
        with open(new_film_path, "w", encoding="utf-8") as f:
            yaml.dump(film_data, f, allow_unicode=True, sort_keys=False)
            
        print(f"✨ [RecyclingCar] 新しいネガが地層に定着しました: {new_film_path}")
        return new_film_path
