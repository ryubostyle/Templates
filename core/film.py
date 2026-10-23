# core/film.py
from pathlib import Path
from typing import Any
import yaml

from core.exceptions import FilmValidationError

class FilmLoader:
    """YAMLを安全に読み込み、基本構造を検証するローダー"""

    @staticmethod
    def load(path: Path) -> dict[str, Any]:
        if not path.exists():
            raise FilmValidationError(f"Filmファイルが見つかりません: {path}")
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise FilmValidationError(f"YAMLのパースに失敗しました: {e}")

        if not isinstance(data, dict):
            raise FilmValidationError("Filmのルートは辞書型である必要があります。")

        # 最小限の必須キー検証
        required_keys = ["schema_version", "metadata", "projection", "extensions"]
        for key in required_keys:
            if key not in data:
                raise FilmValidationError(f"必須キー '{key}' がFilmに含まれていません。")

        return data
