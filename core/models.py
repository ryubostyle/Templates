# core/models.py
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class Projection:
    """Screenに渡す変換結果（描画用データ）"""
    project_id: str
    template_id: str
    content: dict[str, Any] = field(default_factory=dict)
