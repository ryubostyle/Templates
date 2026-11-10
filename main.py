# main.py (検証・単体テスト用)
from core.RecyclingPlant.recycling_processor import RecyclingProcessor

if __name__ == "__main__":
    print("🧪 [Test Ignition] 単体テスト用メインスクリプトを起動します...")
    
    root_trushes = ".trushes"
    archives = "library-scroll/archives"
    
    # ボイラーの点火
    processor = RecyclingProcessor(
        root_trushes_dir=root_trushes, 
        archives_dir=archives
    )
    
    result = processor.sweep_and_transform()
    print(f"✨ [Test Result] 処理結果フィルム: {result}")
