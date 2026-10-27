# library-scroll/projector.py
# 「ひとつ上の階層（..）にある core から BaseProjector を継承する」
from ..core.base_projector import BaseProjector

class LibraryScrollProjector(BaseProjector):
    def project(self, film_data):
        # 継承した親の仕組みを使って現像処理を行う
        pass
        
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
