# Chaos/baseChaos.py
import os
import shutil
from abc import ABC, abstractmethod
from . import ENTROPY_ROOT, REPOSITORY_ROOT, NEXT_ROOT


class BaseChaos(ABC):
    """
    Chaos 基底クラス (完全無滞留・物理 sweep-to 準拠):
    内部にデータを一切溜め込まず、検知した揺らぎを
    有無を言わさず NEXT_ROOT へダイレクトに放り投げる純粋な感覚器。
    """
    def __init__(self):
        # __init__.py で静的に定義された三位一体の座標を直接宿す
        self.target_dir = ENTROPY_ROOT       # 現在の聖域座標
        self.repository_root = REPOSITORY_ROOT  # リポジトリ全体の根
        self.next_root = NEXT_ROOT              # 次なる代謝先

    @abstractmethod
    def sense_fluctuation(self) -> bool:
        """聖域内の揺らぎ（ファイル）を感知する"""
        pass

    def sweep_to_next(self, file_path: str) -> None:
        """
        聖域を犯したファイルを一切溜め込まず、有無を言わさず NEXT_ROOT へ物理 sweep-to する
        """
        if not os.path.exists(self.next_root):
            os.makedirs(self.next_root)
            
        base_name = os.path.basename(file_path)
        if base_name == ".gitkeep":
            return
            
        dest_path = os.path.join(self.next_root, base_name)
        try:
            if os.path.exists(file_path):
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                shutil.move(file_path, dest_path)
                print(f"    🚀 [Chaos Physical Sweep] 滞留なしで NEXT_ROOT へ直行: [{base_name}] -> {self.next_root}")
        except Exception as e:
            print(f"    ⚠️ [Sweep Error] [{base_name}]: {e}")
