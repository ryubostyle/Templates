import os
import traceback
from datetime import datetime
import yaml

class ErrorTrapper:
    """
    システム全体のエラーや例外を捕縛し、
    静寂の地層へ `.film.yaml` としてネガ（記録）を定着させるセーフティネット（水脈）
    """

    @staticmethod
    def trap(archives_dir: str = "library-scroll/archives", error_context: str = "Unknown Context", exception: Exception = None):
        """
        例外を受け取り、YAML形式のフィルムとしてアーカイブへ書き出す
        """
        os.makedirs(archives_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        film_filename = f"error_{timestamp}.film.yaml"
        film_path = os.path.join(archives_dir, film_filename)

        error_message = str(exception) if exception else "No exception provided"
        tb_str = traceback.format_exc() if exception else "No traceback available"

        film_data = {
            "type": "error_trap",
            "context": error_context,
            "timestamp": datetime.now().isoformat(),
            "error": {
                "message": error_message,
                "traceback": tb_str.splitlines()
            }
        }

        try:
            with open(film_path, "w", encoding="utf-8") as f:
                yaml.dump(film_data, f, allow_unicode=True, sort_keys=False)
            print(f"[ErrorTrapper] 破綻を検知し、フィルムを定着させました: {film_path}")
        except Exception as e:
            print(f"[ErrorTrapper Fatal] フィルムの書き出しに失敗しました: {e}")

    @staticmethod
    def _zen_void(archives_dir: str = "library-scroll/archives", message: str = "Zero point quiet state."):
        """
        処理すべきカオスやエラーがなく、静寂（零点）が保たれているときの記録
        """
        os.makedirs(archives_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        film_path = os.path.join(archives_dir, f"zen_void_{timestamp}.film.yaml")

        film_data = {
            "type": "zen_void",
            "message": message,
            "timestamp": datetime.now().isoformat()
        }

        with open(film_path, "w", encoding="utf-8") as f:
            yaml.dump(film_data, f, allow_unicode=True, sort_keys=False)
