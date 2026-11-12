# Processor/baseProcessor.py
import os
import shutil
from abc import ABC, abstractmethod
from . import ENTROPY_ROOT, REPOSITORY_ROOT, NEXT_ROOT


class BaseProcessor(ABC):
    """
    Processor 基底クラス (完全無滞留・物理 sweep-to 準拠):
    代謝・変換された実体を一切滞留させず、有無を言わさず
    NEXT_ROOT（StrataCrystallization 聖域）へダイレクトに物理 sweep-to する感覚器。
    """
    def __init__(self):
        self.target_dir = ENTROPY_ROOT
        self.repository_root = REPOSITORY_ROOT
        self.next_root = NEXT_ROOT

    @abstractmethod
    def sense_fluctuation(self) -> bool:
        """プロセッサ聖域内の揺らぎを感知する"""
        pass

    def sweep_to_next(self, file_path: str) -> None:
        """
        代謝物を滞留なしで NEXT_ROOT へ物理 sweep-to する
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
                print(f"    ⚙️ [Processor Physical Sweep] 代謝物を NEXT_ROOT へ直行: [{base_name}] -> {self.next_root}")
        except Exception as e:
            print(f"    ⚠️ [Processor Sweep Error] [{base_name}]: {e}")
