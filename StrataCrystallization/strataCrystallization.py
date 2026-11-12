# StrataCrystallization/strataCrystallization.py
import os
from abc import ABC, abstractmethod
from . import ENTROPY_ROOT, REPOSITORY_ROOT, NEXT_ROOT


class StrataCrystallization(ABC):
    """
    StrataCrystallization 聖域クラス (完全表出・sweep-to-screen 準拠):
    結晶化したスクロールや資産を内部に溜め込まず、
    有無を言わさず screen（画面・外界）へ表出（sweep-to-screen）させつつ、
    必要に応じて輪を閉じるため NEXT_ROOT（Chaos）へ回帰させる。
    """
    def __init__(self):
        self.target_dir = ENTROPY_ROOT
        self.repository_root = REPOSITORY_ROOT
        self.next_root = NEXT_ROOT  # Chaos への回帰点

    @abstractmethod
    def sense_crystallization(self) -> bool:
        """結晶化すべき聖域内の実体を感知する"""
        pass

    def sweep_to_screen(self, file_path: str) -> None:
        """
        結晶化された実体をスクリーンの向こうへ表出させ、同時に循環の輪を閉じるために
        次なるはじまり（Chaos / NEXT_ROOT）へも実体を還す
        """
        base_name = os.path.basename(file_path)
        if base_name == ".gitkeep":
            return

        try:
            if os.path.exists(file_path):
                # 1. 画面（Screen）への表出を遂行
                print(f"\n    💎✨ [Crystallization Screen Output] 表出完了 ──────────────────")
                print(f"    📜 結晶体ファイル: [{base_name}]")
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    # プレビューとして冒頭数行、あるいは内容を画面に焼き付ける
                    print(f"    --------------------------------------------------")
                    print(content[:500] + ("..." if len(content) > 500 else ""))
                    print(f"    --------------------------------------------------\n")

                # 2. 循環の輪を閉じるため、次の循環基点（Chaos / NEXT_ROOT）へも還元
                if not os.path.exists(self.next_root):
                    os.makedirs(self.next_root)
                
                dest_path = os.path.join(self.next_root, base_name)
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                
                import shutil
                shutil.move(file_path, dest_path)
                print(f"    🔄 [Eternal Circulation] 輪が閉じられました: [{base_name}] -> 循環の起点 (Chaos)")

        except Exception as e:
            print(f"    ⚠️ [Screen Output Error] [{base_name}]: {e}")
