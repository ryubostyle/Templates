# Chaos/baseChaos.py
import os
import shutil
from abc import ABC, abstractmethod
from typing import Dict, List


class BaseChaos(ABC):
    """
    Chaos 基底クラス (退避聖域 trushes/ 対応版):
    混沌の聖域における揺らぎを感知し、テキストシードを収穫すると同時に、
    不要なファイルやバイナリを trushes/ 聖域へと美しく分別・退避させる心臓部。
    """
    def __init__(self, target_dir: str = "Chaos", trash_dir: str = "trushes"):
        self.target_dir = target_dir
        self.trash_dir = os.path.join(target_dir, trash_dir) if not target_dir.endswith(trash_dir) else target_dir
        self.source_paths: List[str] = []
        self.raw_seeds: Dict[str, str] = {}

    @abstractmethod
    def sense_fluctuation(self) -> bool:
        pass

    @abstractmethod
    def absorb_entropy_seed(self) -> Dict[str, str]:
        pass

    def sweep_to_trash(self, file_path: str) -> None:
        """
        不要なファイルやバイナリを Chaos/ 配下の trushes/ 聖域へ隔離・移動する
        """
        if not os.path.exists(self.trash_dir):
            os.makedirs(self.trash_dir)
            
        base_name = os.path.basename(file_path)
        # trushes 自身の中にあるファイルや .gitkeep は対象外にする
        if "trushes" in file_path or base_name == ".gitkeep":
            return
            
        dest_path = os.path.join(self.trash_dir, base_name)
        try:
            if os.path.exists(file_path):
                # 既に同名ファイルがあれば上書きまたは避難
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                shutil.move(file_path, dest_path)
                print(f"    🗑️ [Chaos Trash Sweep] 不要なファイルを trushes/ へ退避しました: [{base_name}] -> [{dest_path}]")
        except Exception as e:
            print(f"    ⚠️ [Trash Error] trushes/ への移動に失敗しました [{base_name}]: {e}")


if __name__ == "__main__":
    print("🌪️ [Chaos 零点] 単体動作テスト: 聖域の監視および trushes 分別テストを開始します。")

    class ConcreteChaos(BaseChaos):
        def sense_fluctuation(self) -> bool:
            if not os.path.exists(self.target_dir):
                return False
            # .gitkeep および trushes フォルダ自体を除外して実ファイルを走査
            files = [
                f for f in os.listdir(self.target_dir) 
                if os.path.isfile(os.path.join(self.target_dir, f)) and f != ".gitkeep"
            ]
            if files:
                self.source_paths = [os.path.join(self.target_dir, f) for f in files]
                print(f"  - 🌪️ 揺らぎ検知: {files}")
                return True
            return False

        def absorb_entropy_seed(self) -> Dict[str, str]:
            for path in self.source_paths:
                # バイナリや画像などの不要ファイルは trushes/ へ逃がす分別処理
                if path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bin', '.exe', '.zip')):
                    self.sweep_to_trash(path)
                    continue

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        self.raw_seeds[path] = f.read()
                    print(f"  - 📜 有効なテキストシードとして収穫: [{os.path.basename(path)}]")
                except UnicodeDecodeError:
                    # デコード不能なバイナリも trushes/ へ掃き出す
                    print(f"  - ⚠️ デコード不能なため trushes/ へ退避します: [{os.path.basename(path)}]")
                    self.sweep_to_trash(path)
            return self.raw_seeds

    chaos = ConcreteChaos("Chaos")
    if chaos.sense_fluctuation():
        chaos.absorb_entropy_seed()
    else:
        print("  - 🍃 聖域は静寂に包まれています。")
