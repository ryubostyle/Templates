from dataclasses import dataclass, field
from typing import Dict, Any, List

@dataclass
class Film:
    film_id: str
    title: str
    source: Dict[str, Any]
    latent_questions: List[str] = field(default_factory=list)
    provenance: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'Film':
        """YAMLから読み込んだ辞書データを、厳格なFilmオブジェクトへ昇華する"""
        return cls(
            film_id=data.get("film_id", "scroll-unknown"),
            title=data.get("title", "無題の地層"),
            source=data.get("source", {}),
            latent_questions=data.get("latent_questions", []),
            provenance=data.get("provenance", {})
        )

