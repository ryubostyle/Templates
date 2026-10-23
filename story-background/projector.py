from pathlib import Path
from typing import Any
from core.base_projector import BaseProjector

class StoryBackgroundProjector(BaseProjector):
    template_id = "story-background"

    def transform(self) -> dict[str, Any]:
        ext = self.film.get("extensions", {}).get("story_background", {})
        metadata = self.film.get("metadata", {})
        
        return {
            "title": metadata.get("title", "無題の物語"),
            "narrative_mode": ext.get("narrative_mode", "chronological"),
            "timeline": ext.get("timeline", []),
            "turning_points": ext.get("turning_points", []),
            "philosophy": self.film.get("philosophy", {}),
        }
