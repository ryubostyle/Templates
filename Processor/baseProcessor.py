# Processor/baseProcessor.py
import os
import shutil
from abc import ABC, abstractmethod


class BaseProcessor(ABC):
    """
    Processor 基底クラス (os.path 安全自立版):
    自身のファイル位置を起点に聖域座標と次なる代謝先を完全自給し、
    滞留なく NEXT_ROOT へ物理 sweep-to する感覚器。
    """
    def __init__(self):
        # スクリプト自身の位置を起点に絶対座標を安全に算出
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.repository_root = os.path.dirname(current_dir)
        
        self.target_dir = current_dir
        self.next_root = os.path.join(self.repository_root, "StrataCrystallization")

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
