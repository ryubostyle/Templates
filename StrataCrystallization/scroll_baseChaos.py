# Chaos/baseChaos.py
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseChaos(ABC):
    """
    Chaos基底クラス:
    外界からの未整流なインプットを受け付け、⊕/⊖のエネルギーバランスを
    保ちながら「揺らぎを感知・保持する」責任を担います。
    """
    def __init__(self, target_dir: str):
        self.target_dir = target_dir
        self.source_paths: List[str] = []
        self.energy_balance = {"positive": 0, "negative": 0}

    @abstractmethod
    def sense_fluctuation(self) -> bool:
        """揺らぎ（インプットの発生）を感知する抽象メソッド"""
        pass

    @abstractmethod
    def absorb_entropy_seed(self) -> Any:
        """混沌の中から次の下流へ流すための原初データを吸い込むメソッド"""
        pass


if __name__ == "__main__":
    print("🌪️ [Chaos 零点] 全方位・自己言及的スキャンによる単体テストを開始します...")

    class AllInclusiveChaos(BaseChaos):
        def sense_fluctuation(self) -> bool:
            if not os.path.exists(self.target_dir):
                return False
            
            files = [f for f in os.listdir(self.target_dir) if os.path.isfile(os.path.join(self.target_dir, f))]
            
            if files:
                self.source_paths = [os.path.join(self.target_dir, f) for f in files]
                print(f"  - 👃 自己感知：零点内で複数の揺らぎを発見しました -> {files}")
                return True
            else:
                print("  - 🍃 零点は静寂に包まれています。")
                return False

        def absorb_entropy_seed(self) -> Dict[str, str]:
            seeds = {}
            for path in self.source_paths:
                if os.path.exists(path):
                    with open(path, "r", encoding="utf-8") as f:
                        seeds[path] = f.read()
            return seeds

    scanner = AllInclusiveChaos(".")
    
    if scanner.sense_fluctuation():
        all_seeds = scanner.absorb_entropy_seed()
        print(f"  - 抽出された揺らぎの総数: {len(all_seeds)} ファイル")
        print("✨ [Chaos 零点] 独立単体テスト：完全なる自己完結を確認しました。")