import os
from datetime import datetime
import yaml
from jinja2 import Template

def run_library_scroll():
    archives_dir = "library-scroll/archives"
    templates_dir = "library-scroll/templates"
    output_screen = "library-scroll/index.md"
    
    # 1. 部屋（archives）の準備
    os.makedirs(archives_dir, exist_ok=True)
    
    # 2. 本日のネガファイル（archives/yyyy.mm.dd.nn.film.yaml）の決定
    today_str = datetime.now().strftime("%Y.%m.%d")
    existing_files = os.listdir(archives_dir)
    today_prefix = f"{today_str}."
    today_count = sum(1 for f in existing_files if f.startswith(today_prefix) and f.endswith(".yaml"))
    sequence_number = f"{today_count + 1:02d}"
    
    new_film_filename = f"{today_str}.{sequence_number}.film.yaml"
    new_film_path = os.path.join(archives_dir, new_film_filename)
    
    # 3. まだ本日のネガがなければ、思考の断片から自動製版（アーカイブ）する
    # ※ここに、スマホなどから投げ込まれた最新の思考の断片を宿すことができます
    raw_idea = """
    雲の上のGitHub空港から第一機目が離陸した。
    archives/ の下に時間の地層を刻みつつ、不変のエンジンで巻物を現像する。
    静的な記録が、動的なホログラフィック・スクリーンへと昇華する瞬間。
    """
    
    film_data = {
        "film_id": f"scroll-{today_str}-{sequence_number}",
        "title": f"地層の記録 ── {today_str} 第{sequence_number}幕",
        "source": {
            "type": "mobile_chaos_note",
            "content": raw_idea.strip()
        },
        "latent_questions": [
            "記録された過去は、次の航海へどう接続されるか？",
            "零点から発進した思考は、どのような意味の地層を築くか？"
        ],
        "provenance": {
            "source_preserved": True,
            "interpretation_status": "unresolved",
            "generated_by": "library-scroll/run_demo.py"
        }
    }
    
    # ネガフィルムの自動製版・定着
    with open(new_film_path, "w", encoding="utf-8") as f:
        yaml.dump(film_data, f, allow_unicode=True, sort_keys=False)
    print(f"✨ 新しいネガが地層に定着しました: {new_film_path}")

    # 4. 現像（Render）：最新のネガ（または生成したネガ）を読み込んで型枠を通す
    template_path = os.path.join(templates_dir, "scroll.md.j2")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"型枠が見つかりません: {template_path}")
        
    with open(new_film_path, "r", encoding="utf-8") as f:
        current_film = yaml.safe_load(f)
        
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
        
    jinja_template = Template(template_content)
    rendered_screen = jinja_template.render(current_film)
    
    # 5. スクリーン（index.md）へ投影
    with open(output_screen, "w", encoding="utf-8") as f:
        f.write(rendered_screen)
        
    print(f"scroll: 巻物の現像が完了しました -> {output_screen}")

if __name__ == "__main__":
    run_library_scroll()
