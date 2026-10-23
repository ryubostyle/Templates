# library-scroll/projector.py
from pathlib import Path
from typing import Any
from core.base_projector import BaseProjector

class LibraryScrollProjector(BaseProjector):
    template_id = "library-scroll"

    def transform(self) -> dict[str, Any]:
        ext = self.film.get("extensions", {}).get("library_scroll", {})
        metadata = self.film.get("metadata", {})
        
        return {
            "title": metadata.get("title", "無題の巻物"),
            "archive_title": ext.get("archive_title", ""),
            "organization": ext.get("organization", "thematic"),
            "include_toc": ext.get("include_toc", True),
            "philosophy": self.film.get("philosophy", {}),
            "entries": self.film.get("entries", []),
        }
