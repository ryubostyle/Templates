import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.RecyclingPlant.recycling_processor import RecyclingProcessor
from core.error_trapper import ErrorTrapper
from projector import LibraryScrollProjector

def run():
    archives_dir = "library-scroll/archives"
    trushes_dir = "library-scroll/trushes"
    
    try:
        print("🚀 [library-scroll] 多段式プラントの航海を開始します...")
        
        processor = RecyclingProcessor(root_trushes_dir=trushes_dir, archives_dir=archives_dir)
        new_film_path = processor.sweep_and_transform()
        
        projector = LibraryScrollProjector()
        projector.project(new_film_path)
        
        print("✨ [library-scroll] すべての多段式プロセスが正常に完了しました。")

    except Exception as e:
        print(f"⚠️ 異常を検知しました: {e}")
        ErrorTrapper.trap(archives_dir=archives_dir, error_context="library-scroll/run_demo.py execution", exception=e)
        raise e

if __name__ == "__main__":
    run()
