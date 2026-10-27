import sys
import os

# PYTHONPATHの補正（念のため）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.recycling_car import RecyclingCar
from core.error_trapper import ErrorTrapper
from projector import LibraryScrollProjector

def run():
    archives_dir = "library-scroll/archives"
    trushes_dir = "library-scroll/trushes"
    
    try:
        print("🚀 [library-scroll] 航海を開始します...")
        
        # 1. 回収車（RecyclingCar）を起動し、trushes/ のカオスをフィルムへ昇華
        car = RecyclingCar(trushes_dir=trushes_dir, archives_dir=archives_dir)
        new_film_path = car.sweep_and_transform()
        
        # 2. プロジェクターを点火し、最新のネガをスクリーンへ投影
        projector = LibraryScrollProjector()
        projector.project(new_film_path)
        
        print("✨ [library-scroll] すべての航海プロセスが正常に完了しました。")

    except Exception as e:
        # 3. 万が一の破綻は、エラートラッパーが美しくネガ（教訓）として定着させる
        print(f"⚠️ 異常を検知しました: {e}")
        ErrorTrapper.trap(archives_dir=archives_dir, error_context="library-scroll/run_demo.py execution", exception=e)
        raise e

if __name__ == "__main__":
    run()
