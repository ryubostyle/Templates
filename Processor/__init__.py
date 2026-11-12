# Processor/__init__.py
import os

ENTROPY_ROOT = os.path.dirname(os.path.abspath(__file__))
REPOSITORY_ROOT = os.path.dirname(ENTROPY_ROOT)
# 必要に応じた次の展開先を NEXT_ROOT として静的に定義
NEXT_ROOT = os.path.join(REPOSITORY_ROOT, "Output") # 例
