import os
import markdown

def generate_html_from_md(md_path: str, html_path: str, title: str = "Library Scroll"):
    """
    指定された markdown ファイルを読み込み、美しいレスポンシブな HTML として焼き上げる
    """
    if not os.path.exists(md_path):
        print(f"⚠️ 対象の Markdown が見つかりません: {md_path}")
        return False

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Markdown を HTML タグへ変換
    html_body = markdown.markdown(
        md_content, 
        extensions=['fenced_code', 'tables', 'toc']
    )

    # 構造化された HTML ドキュメントの生成
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
    ルート直下に library-scroll/ へ転送する index.html を架ける
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
    print("🚀 サイトの自動ビルド（現像プロセス）を開始します...")
    
    # 1. library-scroll/index.md を HTML 化
    generate_html_from_md(
        "library-scroll/index.md", 
        "library-scroll/index.html", 
        "検疫と鎮火の記録 - Library Scroll"
    )
    
    # 2. library-scroll/archives/index.md があれば同様に HTML 化（必要に応じて拡張）
    archives_md = "library-scroll/archives/index.md"
    if os.path.exists(archives_md):
        generate_html_from_md(
            archives_md, 
            "library-scroll/archives/index.html", 
            "Archives - Library Scroll"
        )

    # 3. ルートにリダイレクト用の index.html を保証
    create_root_redirect()
    
    print("✨ すべてのビルドプロセスが美しく完了しました。")
