from pathlib import Path
from typing import Any
from core.base_projector import BaseProjector

class LogTemplateProjector(BaseProjector):
    template_id = "log-template"

    def transform(self) -> dict[str, Any]:
        ext = self.film.get("extensions", {}).get("log_template", {})
        metadata = self.film.get("metadata", {})
        
        # ソート順に応じたイベントの並び替え（デフォルトは昇順）
        events = ext.get("events", [])
        sort_order = ext.get("sort_order", "ascending")
        if sort_order == "descending":
            events = sorted(events, key=lambda x: x.get("timestamp", ""), reverse=True)
        else:
            events = sorted(events, key=lambda x: x.get("timestamp", ""))

        return {
            "title": metadata.get("title", "無題の航行日誌"),
            "timezone": ext.get("timezone", "+09:00"),
            "sort_order": sort_order,
            "events": events,
            "philosophy": self.film.get("philosophy", {}),
        }
