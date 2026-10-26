from pathlib import Path
import sys
import yaml

# 同じモジュール内（または直下の projector）を確実にインポートする
current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(current_dir))

from projector import LibraryScrollProjector
