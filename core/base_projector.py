# core/base_projector.py
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from core.models import Projection
from core.film import FilmLoader

class BaseProjector(ABC):
    """全テンプレートが継承する共通基底クラス"""

    template_id: str = "base"

    def __init__(self, film: dict[str, Any]):
        self.film = film

    @classmethod
    def from_yaml(cls, path: Path) -> "BaseProjector":
        """YAMLを読み込み、インスタンス化する共通ファクトリ"""
        film_data = FilmLoader.load(path)
        
        # template_id の一致確認
        actual_template_id = film_data.get("metadata", {}).get("template_id")
        if actual_template_id != cls.template_id:
            raise ValueError(
                f"template_id のミスマッチです。期待値: '{cls.template_id}', 検出値: '{actual_template_id}'"
            )
            
        return cls(film_data)

    @abstractmethod
    def transform(self) -> dict[str, Any]:
        """子クラス固有の変換規則を実装する"""
        pass

    def project(self) -> Projection:
        """共通の投射パイプライン"""
        content = self.transform()
        metadata = self.film.get("metadata", {})

        return Projection(
            project_id=metadata.get("project_id", "unknown-project"),
            template_id=self.template_id,
            content=content,
        )
