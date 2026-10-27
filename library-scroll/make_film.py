import os
from datetime import datetime
import yaml

def generate_new_film(raw_content, title="無題の地層", category="philosophical_note"):
    """
    カオスな生原稿から、archives/yyyy.mm.dd.nn.film.yaml を自動生成する
    """
    # 1. 部屋（ディレクトリ）の準備
    archives_dir = "library-scroll/archives"
    os.makedirs(archives_dir, exist_ok=True)
    
    # 2. 日付ベースのファイル名と連番（nn）の決定
    today_str = datetime.now().strftime("%Y.%m.%d")
    
    # 本日の既存ファイルをスキャンして次の連番を決定
    existing_files = os.listdir(archives_dir)
    today_prefix = f"{today_str}."
    today_count = sum(1 for f in existing_files if f.startswith(today_prefix))
    sequence_number = f"{today_count + 1:02d}" # 01, 02, 03...
    
    filename = f"{today_str}.{sequence_number}.film.yaml"
    file_path = os.path.join(archives_dir, filename)
    
    # 3. 幹（core）の仕様に準拠したフィルム構造の構築
    film_data = {
        "film_id": f"scroll-{today_str}-{sequence_number}",
        "title": title,
        "source": {
            "type": category,
            "content": raw_content.strip()
        },
        "latent_questions": [
            "この記録からどのような意味の地層が立ち上がるか？",
            "過去の断片は、次の航海へどう接続されるか？"
        ],
        "provenance": {
            "source_preserved": True,
            "interpretation_status": "unresolved",
            "generated_by": "library-scroll/make_film.py"
        }
    }
    
    # 4. archives/ の空域へ YAML として保存（現像・定着）
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(film_data, f, allow_unicode=True, sort_keys=False)
        
    print(f"✨ 新しいネガフィルムが地層に定着しました: {file_path}")
    return file_path

if __name__ == "__main__":
    # --- テスト用の生原稿（カオスな思考の断片） ---
    sample_chaos = """
    海原から空域へと視界が開けた。
    静的な記録をただ保存するのではなく、archives/ の下へ下へと地層のように積んでいく。
    スマホから投げ込まれたテキストが、自動でネガフィルムに生まれ変わる瞬間。
    """
    
    # 自動生成の実行
    generate_new_film(
        raw_content=sample_chaos,
        title="地層の自動定着とネガの錬金術",
        category="mobile_chaos_note"
    )
