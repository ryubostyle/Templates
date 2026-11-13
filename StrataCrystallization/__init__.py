# Chaos/__init__.py
import os

# 1. 現在の聖域自身のルート
ENTROPY_ROOT = os.path.dirname(os.path.abspath(__file__))

# 2. リポジトリ全体のルート
REPOSITORY_ROOT = os.path.dirname(ENTROPY_ROOT)

# 3. 次の代謝先（Entropy 聖域）
NEXT_ROOT = os.path.join(REPOSITORY_ROOT, "Entropy")
