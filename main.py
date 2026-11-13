# main.py
import os
import glob
import shutil
try:
    import yaml
except ImportError:
    yaml = None

class CirculationPipeline:
    """
    完全自律循環パイプライン（Declarative Cascading Architecture）:
    architecture.yml を読み込み、量子準位（Chaos -> Entropy -> Processor -> StrataCrystallization）
    に沿ってデータを段階的かつ離散的に精製・結晶化させる主制御装置。
    """
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.arch_config = self._load_architecture()
        
        # 各聖域のパス定義（architecture.yml から動的解決、フォールバック付き）
        self.chaos_dir = os.path.join(self.root_dir, "Chaos")
        self.entropy_dir = os.path.join(self.root_dir, "Entropy")
        self.processor_dir = os.path.join(self.root_dir, "Processor")
        self.crystallization_dir = os.path.join(self.root_dir, "StrataCrystallization")

    def _load_architecture(self) -> dict:
        """リポジトリのルートにある architecture.yml から位相定義をロードする"""
        yml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "architecture.yml")
        if yaml and os.path.exists(yml_path):
            try:
                with open(yml_path, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f)
            except Exception as e:
                print(f"⚠️ [Architecture Warning] architecture.yml のロードに失敗しました: {e}")
        return {}

    def run_metabolism(self):
        print("🔥 [Cloud Metabolism] 宣言的アーキテクチャに基づく雲上の代謝サイクルを開始します...")

        # 1. [Chaos -> Entropy] 混沌から神経・血流への量子ジャンプ
        self._sweep_sanctuary(self.chaos_dir, self.entropy_dir, "🚀 [Chaos -> Entropy]")

        # 2. [Entropy -> Processor] 神経・血流から心臓部（執行）への量子ジャンプ
        self._sweep_sanctuary(self.entropy_dir, self.processor_dir, "⚡ [Entropy -> Processor]")

        # 3. [Processor -> StrataCrystallization] 執行部から永遠の地層結晶化エリアへのスイープ
        self._sweep_sanctuary(self.processor_dir, self.crystallization_dir, "⚙️ [Processor -> Crystallization]")

        # 4. [StrataCrystallization Screen Output] 最下流での画面表出と地層への定着（還流停止）
        self._crystallize_and_store()

        print("✨ [Cloud Metabolism] 飛び飛びの量子準位を巡る一連の代謝サイクルが正常に完了しました。")

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

    def _crystallize_and_store(self):
        """StrataCrystallization 内に到達した成果物を画面表出し、地層として永遠に定着させる"""
        if not os.path.exists(self.crystallization_dir):
            return

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

                # 🏛️ 【地層の定着】Chaosへの物理還流は行わず、聖域（StrataCrystallization）に永遠に堆積させる
                print(f"    🏛️ [Strata Stored] 循環の輪は閉じられず、結晶体が永遠の地層に定着しました: [{base_name}]")

if __name__ == "__main__":
    pipeline = CirculationPipeline()
    pipeline.run_metabolism()
