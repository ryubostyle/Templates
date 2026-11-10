# main.py (パイプライン＆サイトビルダー統合版)
import os
import markdown
from core.RecyclingPlant.recycling_processor import RecyclingProcessor

def sweep_and_recycle(root_trushes: str, archives_dir: str):
    """
    これまでの多段式プロセッサ（RecyclingProcessor）によるゴミ箱の掃き掃除と昇華プロセス
    """
    print("🧹 [Pipeline] 零点 (.trushes) の掃き掃除と昇華を開始します...")
    processor = RecyclingProcessor(
        root_trushes_dir=root_trushes, 
        archives_dir=archives_dir
    )
    result = processor.sweep_and_transform()
    print(f"✨ [Pipeline Result] 処理されたフィルム: {result}")
    return result

def generate_html_from_md(md_path: str, html_path: str, title: str = "Library Scroll"):
    """
    library-scroll/ 配下の index.md を美しくレスポンシブな HTML へ現像する
    """
    if not os.path.exists(md_path):
        print(f"⚠️ [Build] 対象の Markdown が見つかりません: {md_path}")
        return False

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Markdown を HTML タグへ変換
    html_body = markdown.markdown(
        md_content, 
        extensions=['fenced_code', 'tables', 'toc']
    )

    html_document = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.7;
            color: #24292e;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            background: #fbfbfb;
        }}
        h1, h2, h3 {{ border-bottom: 1px solid #eaeaea; padding-bottom: .3em; }}
        code {{ background: #f6f8fa; padding: 0.2em 0.4em; border-radius: 3px; font-size: 85%; }}
        pre {{ background: #f6f8fa; padding: 16px; border-radius: 6px; overflow-x: auto; }}
        blockquote {{ border-left: 4px solid #dfe2e5; color: #6a737d; margin: 0; padding-left: 16px; }}
        hr {{ border: 0; height: 1px; background: #eaeaea; margin: 24px 0; }}
    </style>
</head>
<body>
    {html_body}
</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_document)
    
    print(f"✨ [Build] 現像完了: {html_path}")
    return True

def create_root_redirect():
    """
    404 を回避するため、ルート直下に library-scroll/ へ転送する index.html を架ける
    """
    root_html_path = "index.html"
    redirect_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=./library-scroll/">
    <title>Redirecting to Library Scroll...</title>
</head>
<body>
    <p>Redirecting to <a href="./library-scroll/">library-scroll/</a>...</p>
</body>
</html>
"""
    with open(root_html_path, "w", encoding="utf-8") as f:
        f.write(redirect_content)
    print(f"🌐 [Redirect] ルートへの看板を架けました: {root_html_path}")

if __name__ == "__main__":
    print("🚀 [Ignition] 統合型マネージャー＆ビルダーを起動します...")
    
    root_trushes = ".trushes"
    archives = "library-scroll/archives"
    
    # 1. ゴミ箱の回収・昇華パイプラインの実行
    sweep_and_recycle(root_trushes, archives)
    
    # 2. library-scroll/index.md の HTML 現像
    generate_html_from_md(
        "library-scroll/index.md", 
        "library-scroll/index.html", 
        "検疫と鎮火の記録 - Library Scroll"
    )
    
    # 3. archives/index.md があれば同様に現像
    archives_md = "library-scroll/archives/index.md"
    if os.path.exists(archives_md):
        generate_html_from_md(
            archives_md, 
            "library-scroll/archives/index.html", 
            "Archives - Library Scroll"
        )

    # 4. ルートへのリダイレクト看板の保証
    create_root_redirect()
    
    print("✨ すべてのプロセスが美しく完了しました。")
