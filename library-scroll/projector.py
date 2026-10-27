from core.base_projector import BaseProjector

class LibraryScrollProjector(BaseProjector):
    """ライブラリ・スクロール機体専用のプロジェクター"""
    def __init__(self):
        # 親の仕組みに「型枠」と「出力先スクリーンのパス」を教える
        super().__init__(
            template_path="library-scroll/templates/scroll.md.j2",
            output_path="library-scroll/index.md"
        )

