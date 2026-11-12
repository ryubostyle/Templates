# Processor/baseProcessor.py
import os
import sys
from abc import ABC, abstractmethod
from typing import Dict, Any

# パスの自己言及的解決
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Chaos.baseChaos import BaseChaos
from Entropy.baseEntropy import BaseEntropy


class BaseProcessor(ABC):
    """
    Processor基底クラス (完全自律代謝版):
    Chaosの感知、Entropyの整流、StrataCrystallization/ への結晶化定着を経て、
    読み込んだ原初シードを自動消去し、聖域の足元を常にゼロにリセットする心臓部。
    """
    def __init__(self, target_scroll_dir: str = "StrataCrystallization"):
        self.target_scroll_dir = target_scroll_dir
        self.channeled_data: Dict[str, Any] = {}

    @abstractmethod
    def orchestrate_cycle(self) -> bool:
        pass

    @abstractmethod
    def crystallize_scroll(self, identifier: str, content: str) -> str:
        pass

    @abstractmethod
    def reset_chaos_sanctuary(self, processed_paths: list) -> None:
        pass


if __name__ == "__main__":
    print("🔥 [Processor 零点 / 完全自律代謝] 自律循環オーケストレーションを開始します...")

    # 👇 本番用 Chaos 具象クラス（Chaos/ フォルダ内の実ファイルをスキャン）
    class ProductionChaos(BaseChaos):
        def sense_fluctuation(self) -> bool:
            if not os.path.exists(self.target_dir):
                return False
            # .gitkeep を除外して実ファイルのみを感知
            files = [f for f in os.listdir(self.target_dir) if os.path.isfile(os.path.join(self.target_dir, f)) and f != ".gitkeep"]
            if files:
                self.source_paths = [os.path.join(self.target_dir, f) for f in files]
                print(f"  - 🌪️ [Chaos 本番感知] 混沌の聖域にて揺らぎ（実ファイル）を検知しました -> {files}")
                return True
            else:
                print("  - 🍃 Chaos の聖域は静寂に包まれています。")
                return False

        def absorb_entropy_seed(self) -> Dict[str, str]:
            seeds = {}
            for path in self.source_paths:
                if os.path.exists(path):
                    try:
                        # まず UTF-8 テキストとして読み込みを試みる
                        with open(path, "r", encoding="utf-8") as f:
                            content = f.read()
                        seeds[path] = content
                        print(f"    ✓ テキストシード収穫成功: [{os.path.basename(path)}]")
                    except UnicodeDecodeError:
                        # 🛑 UnicodeDecodeError のトラップ処理もここに完全に飲み込ませる
                        print(f"    ⚠️ [Open Flow Bypass] バイナリ/デコード不能なファイルを検出しましたが、完全通過させます: [{os.path.basename(path)}]")
                        # バイナリの場合は空文字またはダミーとして通す、あるいはスキップして後続の処理に委ねる
                        seeds[path] = "[Binary/Non-Text Content Bypassed]"
                    except Exception as e:
                        print(f"    ⚠️ [General Exception Bypass] 予期せぬ例外: [{os.path.basename(path)}] -> {e}")
            return seeds

    # 👇 本番用 Entropy 具象クラス（実シードの整流と例外捕捉）
    class ProductionEntropy(BaseEntropy):
        def channel_flow(self) -> bool:
            print("  - 🌊 [Entropy 本番配管] 原初シードの検針と整流を開始します。")
            if not self.raw_seeds:
                return False

            for path, content in self.raw_seeds.items():
                try:
                    cleaned_content = content.strip()
                    self.channeled_data[path] = {
                        "status": "success",
                        "payload": cleaned_content,
                        "length": len(cleaned_content)
                    }
                    print(f"    ✓ 本番整流成功: [{path}] -> 安全な配管を通過しました。")
                except Exception as e:
                    self.trap_errors(path, str(e))

            return len(self.channeled_data) > 0

        def trap_errors(self, target_path: str = "", error_msg: str = "") -> None:
            if target_path and error_msg:
                err_log = f"Path: {target_path} | Cause: {error_msg}"
                self.trapped_errors.append(err_log)
                print(f"    🛡️ [ErrorTrapper] 隔離しました: {err_log}")

    # 👇 完全自律代謝型 Processor 統括具象クラス
    class AutonomicStrataProcessor(BaseProcessor):
        def orchestrate_cycle(self) -> bool:
            print("  - 🎼 [Processor] 循環のタクトを振ります。実戦モードで Chaos/ をスキャンします。")
            
            chaos_dir = "Chaos"
            chaos = ProductionChaos(chaos_dir)
            if not chaos.sense_fluctuation():
                print("  - 🍃 処理すべき揺らぎ（シード）が検知されませんでした。")
                return False
            
            raw_seeds = chaos.absorb_entropy_seed()
            print(f"  - 🌊 [Processor] 収穫した本番シードを Entropy 配管へ流し込みます (件数: {len(raw_seeds)})。")
            
            entropy = ProductionEntropy(raw_seeds)
            if not entropy.channel_flow():
                print("  - 🛡️ 配管プロセスで異常が検知されました。")
                return False
            
            self.channeled_data = entropy.channeled_data
            print("  - ⚙️ [Processor] 整流済みデータを受け取りました。StrataCrystallization/ への結晶化定着を開始します。")
            
            processed_files = []
            for path, info in self.channeled_data.items():
                base_name = os.path.basename(path)
                scroll_name = f"scroll_{base_name}"
                self.crystallize_scroll(scroll_name, info["payload"])
                processed_files.append(path)

            # 🌟 代謝の完成：結晶化を終えた元シードを Chaos 聖域から昇華・消去する
            self.reset_chaos_sanctuary(processed_files)

            return True

        def crystallize_scroll(self, identifier: str, content: str) -> str:
            if not os.path.exists(self.target_scroll_dir):
                os.makedirs(self.target_scroll_dir)
            
            scroll_path = os.path.join(self.target_scroll_dir, identifier)
            with open(scroll_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"    🏛️ [Strata Crystallization] 結晶化定着完了 -> [{scroll_path}]")
            return scroll_path

        def reset_chaos_sanctuary(self, processed_paths: list) -> None:
            print("  - 🌪️ [Chaos Self-Cleaning] 代謝フェーズ：消費された原初シードを浄化します。")
            for path in processed_paths:
                if os.path.exists(path) and not path.endswith(".gitkeep"):
                    os.remove(path)
                    print(f"    ✨ 昇華完了（消去）: [{path}] -> Chaos の足元がゼロベースにリセットされました。")

    # 完全自律代謝オーケストレーションの駆動
    master = AutonomicStrataProcessor("StrataCrystallization")
    if master.orchestrate_cycle():
        print("✨ [Processor 零点] 完全代謝：三位一体の循環、結晶化定着、および足元の零点リセットが完遂しました。")
    else:
        print("🍃 循環すべきシードが不在のため、聖域は静寂を保っています。")
