# main.py
import os
import glob
import shutil

class CirculationPipeline:
    """
    完全自律循環パイプライン:
    Chaos から始まり、Entropy, Processor を経て StrataCrystallization に至り、
    最終的に screen 表出と Chaos への回帰を完結させる主制御装置。
    """
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 各聖域のパス定義
        self.chaos_dir = os.path.join(self.root_dir, "Chaos")
        self.entropy_dir = os.path.join(self.root_dir, "Entropy")
        self.processor_dir = os.path.join(self.root_dir, "Processor")
        self.crystallization_dir = os.path.join(self.root_dir, "StrataCrystallization")

    def run_metabolism(self):
        print("🔥 [Cloud Metabolism] 雲上の代謝サイクルを開始します...")

        # 1. [Chaos -> Entropy] 混沌から零点へのスイープ
        self._sweep_sanctuary(self.chaos_dir, self.entropy_dir, "🚀 [Chaos -> Entropy]")

        # 2. [Entropy -> Processor] 零点から代謝制御へのスイープ
        self._sweep_sanctuary(self.entropy_dir, self.processor_dir, "⚡ [Entropy -> Processor]")

        # 3. [Processor -> StrataCrystallization] 代謝物から結晶化へのスイープ
        self._sweep_sanctuary(self.processor_dir, self.crystallization_dir, "⚙️ [Processor -> Crystallization]")

        # 4. [StrataCrystallization -> Screen & Chaos] 結晶化の表出と回帰
        self._crystallize_and_circulate()

        print("✨ [Cloud Metabolism] 一連の代謝サイクルが正常に完了しました。")

    def _sweep_sanctuary(self, src_dir: str, dest_dir: str, label: str):
        """指定された聖域間の物理 sweep-to を実行する"""
        if not os.path.exists(src_dir):
            return
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # .gitkeep 以外のすべてのファイルを対象にする
        files = glob.glob(os.path.join(src_dir, "*"))
        for file_path in files:
            if os.path.isfile(file_path):
                base_name = os.path.basename(file_path)
                if base_name == ".gitkeep":
                    continue
                
                dest_path = os.path.join(dest_dir, base_name)
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                
                shutil.move(file_path, dest_path)
                print(f"    {label} 移送: [{base_name}] -> {os.path.basename(dest_dir)}")

    def _crystallize_and_circulate(self):
        """StrataCrystallization 内の成果物を画面表出し、Chaos へ回帰させる"""
        if not os.path.exists(self.crystallization_dir):
            return
        if not os.path.exists(self.chaos_dir):
            os.makedirs(self.chaos_dir)

        files = glob.glob(os.path.join(self.crystallization_dir, "*"))
        for file_path in files:
            if os.path.isfile(file_path):
                base_name = os.path.basename(file_path)
                if base_name == ".gitkeep":
                    continue

                # 1. 画面 (Screen) への表出
                print(f"\n    💎✨ [Crystallization Screen Output] 表出完了 ──────────────────")
                print(f"    📜 結晶体ファイル: [{base_name}]")
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        print(f"    --------------------------------------------------")
                        print(content[:500] + ("..." if len(content) > 500 else ""))
                        print(f"    --------------------------------------------------\n")
                except Exception as e:
                    print(f"    (Binary or unreadable asset: {e})")

                # 🔄 【変更】循環の輪（Chaosへの物理還流）をここで停止し、聖域に定着させる
                # dest_path = os.path.join(self.chaos_dir, base_name)
                # if os.path.exists(dest_path):
                #     os.remove(dest_path)
                # 
                # shutil.move(file_path, dest_path)
                # print(f"    🔄 [Eternal Circulation] 輪が閉じられました: [{base_name}] -> 循環の起点 (Chaos)")

if __name__ == "__main__":
    pipeline = CirculationPipeline()
    pipeline.run_metabolism()
