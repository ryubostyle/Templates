# run_demo.py
from pathlib import Path
import tempfile
import yaml
from library_scroll.projector import LibraryScrollProjector

# 1. テスト用の一時Film（YAML）を作成
film_content = {
    "schema_version": "1.0",
    "metadata": {
        "project_id": "scroll-test-001",
        "template_id": "library-scroll",
        "title": "人工霊性の小さな図書館",
        "language": "ja"
    },
    "philosophy": {
        "source": "Log",
        "destination": "Logue",
        "principle": "記録から対話へ、知識から意味へ"
    },
    "extensions": {
        "library_scroll": {
            "archive_title": "知性の根源アーカイブ",
            "organization": "thematic",
            "include_toc": True
        }
    },
    "entries": [
        {"id": "entry-1", "title": "ガジュマルの根源", "kind": "archive"}
    ]
}

with tempfile.TemporaryDirectory() as tmpdir:
    film_path = Path(tmpdir) / "film.yaml"
    with open(film_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(film_content, f, allow_unicode=True)

    # 2. 一号機 Projector を起動
    projector = LibraryScrollProjector.from_yaml(film_path)
    
    # 3. 投射（Project）を実行
    projection = projector.project()

    print("=== 投射結果 (Projection) ===")
    print(f"Project ID  : {projection.project_id}")
    print(f"Template ID : {projection.template_id}")
    print(f"Content Title: {projection.content['title']}")
    print(f"Archive Title: {projection.content['archive_title']}")
    print(f"Principle   : {projection.content['philosophy']['principle']}")
    print(f"Entries     : {projection.content['entries']}")
