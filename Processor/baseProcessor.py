# Processor/baseProcessor.py
import os
from abc import ABC, abstractmethod
from typing import Dict, Any

# 同階層・他零点からのインポート（パスの相対関係に依存せず自己言及的に解決）
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Chaos.baseChaos import BaseChaos
from Entropy.baseEntropy import BaseEntropy


class BaseProcessor(ABC):
    """
    Processor基底クラス:
    三位一体の循環を統括する指揮者（オーケストレーター）としての責任を担い、
    Chaosの感知、Entropyの整流を経て、最終的なスクロールを library-scroll/ へ定着させる。
    """
    def __init__(self, target_scroll_dir: str = "library-scroll"):
        self.target_scroll_dir = target_scroll_dir
        self.channeled_data: Dict[str, Any] = {}

    @abstractmethod
    def orchestrate_cycle(self) -> bool:
        """Chaos -> Entropy -> Processor の全循環を駆動する抽象メソッド"""
        pass

    @abstractmethod
    def write_to_scroll(self, identifier: str, content: str) -> str:
        """処理された変容体を library-scroll/ の地層に物理的に定着させるメソッド"""
        pass


if __name__ == "__main__":
    print("🔥 [Processor 零点] 自律循環オーケストレーションおよびスクロール定着テストを開始します...")

    # 👇 Chaos の具象クラス（内部定義またはインポート）
    class LocalChaos(BaseChaos):
        def sense_fluctuation(self) -> bool:
            return True
        def absorb_entropy_seed(self) -> dict:
            return {
                "sample_log.txt": "Oriented-Philosophia: 零点からの自律循環テストデータです。"
            }

    # 👇 Entropy の具象クラス
    class LocalEntropy(BaseEntropy):
        def channel_flow(self) -> bool:
            for path, content in self.raw_seeds.items():
                self.channeled_data[path] = {
                    "status": "success",
                    "payload": f"【整流済】\n{content}",
                    "length": len(content)
                }
            return True
        def trap_errors(self, target_path: str = "", error_msg: str = "") -> None:
            pass

    # 👇 Processor によるオーケストレーションの具象実装
    class ScrollMasterProcessor(BaseProcessor):
        def orchestrate_cycle(self) -> bool:
            print("  - 🎼 [Processor] 循環のタクトを振ります。まず Chaos を起動し、揺らぎを感知します。")
            chaos = LocalChaos(".")
            if not chaos.sense_fluctuation():
                print("  - 🍃 揺らぎが検知されませんでした。")
                return False
            
            raw_seeds = chaos.absorb_entropy_seed()
            print(f"  - 🌊 [Processor] 収穫したシードを Entropy 配管へ流し込みます (件数: {len(raw_seeds)})。")
            
            entropy = LocalEntropy(raw_seeds)
            if not entropy.channel_flow():
                print("  - 🛡️ 配管プロセスで破綻が検知されました。")
                return False
            
            self.channeled_data = entropy.channeled_data
            print("  - ⚙️ [Processor] 整流済みデータを受け取りました。library-scroll/ への定着を開始します。")
            
            # 各データをスクロールとして書き出す
            for path, info in self.channeled_data.items():
                base_name = os.path.basename(path)
                scroll_name = f"scroll_{base_name}.md"
                self.write_to_scroll(scroll_name, info["payload"])

            return True

        def write_to_scroll(self, identifier: str, content: str) -> str:
            # library-scroll ディレクトリがなければ自己生成する（地層の形成）
            if not os.path.exists(self.target_scroll_dir):
                os.makedirs(self.target_scroll_dir)
            
            scroll_path = os.path.join(self.target_scroll_dir, identifier)
            with open(scroll_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"    📜 [Scroll Archive] 定着完了 -> [{scroll_path}]")
            return scroll_path

    # オーケストレーションの駆動
    master = ScrollMasterProcessor("library-scroll")
    if master.orchestrate_cycle():
        print("✨ [Processor 零点] 三位一体の循環および library-scroll への定着テストが完遂しました。")
    else:
        print("❌ 循環プロセスに異常が発生しました。")
