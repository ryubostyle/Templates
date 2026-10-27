import os
from datetime import datetime
import yaml
from projector import LibraryScrollProjector

def run():
    archives_dir = "library-scroll/archives"
    os.makedirs(archives_dir, exist_ok=True)
    
    # 1. 本日のネガファイル名（地層）の決定（上書き防止の通し番号）
    today_str = datetime.now().strftime("%Y.%m.%d")
    existing_files = os.listdir(archives_dir)
    today_prefix = f"{today_str}."
    today_count = sum(1 for f in existing_files if f.startswith(today_prefix) and f.endswith(".yaml"))
    sequence_number = f"{today_count + 1:02d}"
    
    new_film_filename = f"{today_str}.{sequence_number}.film.yaml"
    new_film_path = os.path.join(archives_dir, new_film_filename)
    
    # 2. 新しいネガフィルムのデータ構造（思考の断片）
    film_data = {
        "film_id": f"scroll-{today_str}-{sequence_number}",
        "title": f"地層の記録 ── {today_str} 第{sequence_number}幕",
        "source": {
            "type": "genesis_note",
            "content": "零点からの再構築。幹（core）の理を継承し、すべての機体が自立して時間を刻み始める。"
        },
        "latent_questions": [
            "オブジェクト指向の血統は、どのように次の機体へ受け継がれるか？",
            "静的なコードが織りなす時間の地層は、未来の我々に何を語るか？"
        ],
        "provenance": {
            "source_preserved": True,
            "interpretation_status": "harmonized",
            "generated_by": "library-scroll/run_demo.py"
        }
    }
    
    # 3. ネガの自動製版・定着
    with open(new_film_path, "w", encoding="utf-8") as f:
        yaml.dump(film_data, f, allow_unicode=True, sort_keys=False)
    print(f"✨ [archives] 新しいネガが地層に定着しました: {new_film_path}")

    # 4. プロジェクターの点火（現像と投影）
    projector = LibraryScrollProjector()
    projector.project(new_film_path)

if __name__ == "__main__":
    run()

