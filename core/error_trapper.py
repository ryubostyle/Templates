import os
from datetime import datetime
import yaml
import traceback

class ErrorTrapper:
    """システム全体の例外を捕縛し、地層（archives）へエラーフィルムとして記録する親クラス"""
    
    @staticmethod
    def trap(archives_dir: str, error_context: str, exception: Exception):
        os.makedirs(archives_dir, exist_ok=True)
        
        today_str = datetime.now().strftime("%Y.%m.%d")
        existing_files = os.listdir(archives_dir)
        today_prefix = f"{today_str}."
        today_count = sum(1 for f in existing_files if f.startswith(today_prefix) and f.endswith(".yaml"))
        sequence_number = f"{today_count + 1:02d}"
        
        error_film_filename = f"{today_str}.{sequence_number}.film.yaml"
        error_film_path = os.path.join(archives_dir, error_film_filename)
        
        tb_str = "".join(traceback.format_exception(type(exception), exception, exception.__traceback__))
        
        error_film_data = {
            "film_id": f"error-{today_str}-{sequence_number}",
            "title": f"⚠️ 異常検知の記録 ── {today_str} 第{sequence_number}幕",
            "source": {
                "type": "error_log",
                "context": error_context,
                "content": str(exception),
                "traceback": tb_str
            },
            "latent_questions": [
                "この破綻から何を学び、次の設計にどう還元するか？",
                "システムが直面したノイズは、どのような変革の契機となるか？"
            ],
            "provenance": {
                "source_preserved": True,
                "interpretation_status": "error_trapped",
                "generated_by": "core.ErrorTrapper"
            }
        }
        
        with open(error_film_path, "w", encoding="utf-8") as f:
            yaml.dump(error_film_data, f, allow_unicode=True, sort_keys=False)
        
        print(f"🛡️ [ErrorTrapper] エラーを美しくネガとして定着させました: {error_film_path}")
