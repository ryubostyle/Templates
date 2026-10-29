import sys
from pathlib import Path

# プラントのルートディレクトリを Python の検索パスに強制的に通す調律
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

print(f"✨ 庵のルートパスを定位しました: {root_dir}")
print(f"✨ 現在の検索パス (sys.path): {sys.path}")

try:
    # ── プラントの各モジュールのインポートと実行 ──
    # 例: from core.base_projector import ...
    print("🌿 プラントの起動プロセスを開始します...")
    
    # ここに実際の処理（例：ゴミ箱の検疫・ネガ化の呼び出しなど）を記述
    # projector.run() など
    
    print("✨ すべてのプロセスが平穏に完了しました。")

except Exception as e:
    # ほころび（エラー）を優しく捕捉し、詳細なログとしてスクリーンへ映し出す
    print("\n[!] プラントの航海中に予期せぬほころびが検知されました：")
    import traceback
    traceback.print_exc()
    
    # Actions側に明確にエラーを伝えるために異常終了コードを返す
    sys.exit(1)
