# Chaos/__init__.py
import os

# 1. 聖域（Chaos）自身の絶対座標を定義
CHAOS_ROOT = os.path.dirname(os.path.abspath(__file__))

# 2. リポジトリ全体のルート座標（Chaos の親階層）を定義
REPOSITORY_ROOT = os.path.dirname(CHAOS_ROOT)

# 3. 次の零点（Entropy）への代謝先座標を構造として明示する
# （※ Entropy 聖域が存在する/する予定のパス）
ENTROPY_ROOT = os.path.join(REPOSITORY_ROOT, "Entropy")

print(f"  - 🌀 [Chaos Sanctuary Initialized] 聖域座標: {CHAOS_ROOT}")
print(f"  - ⚡ [Next Zero-Point] 次の代謝先（Entropy）: {ENTROPY_ROOT}")
