from pathlib import Path
from typing import Any
import jinja2

from core.models import Projection
from core.exceptions import TemplateError

class ScreenRenderer:
    """ProjectionデータとJinja2テンプレートを結合し、Screen（出力ファイル）を生成するレンダラー"""

    def __init__(self, templates_root: Path):
        """
        templates_root: 各テンプレートのディレクトリが格納されている親パス
        （例: Path(".") または Path("Templates")）
        """
        self.templates_root = templates_root
        
        # Jinja2環境の設定（安全なローダーを使用）
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(str(templates_root)),
            autoescape=jinja2.select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render_to_string(self, template_id: str, projection: Projection, template_filename: str = "scroll.md.j2") -> str:
        """Projectionのコンテンツをテンプレートに適用し、文字列としてレンダリングする"""
        # 各テンプレートディレクトリ（例: library-scroll/templates/scroll.md.j2）から探索
        template_path = f"{template_id}/templates/{template_filename}"
        
        try:
            template = self.env.get_template(template_path)
        except jinja2.TemplateNotFound:
            raise TemplateError(f"指定されたJinja2テンプレートが見つかりません: {template_path}")
        except jinja2.TemplateSyntaxError as e:
            raise TemplateError(f"テンプレートの構文エラー ({template_path}): {e}")

        # Projectionのcontent辞書をテンプレート変数として渡す
        context = {
            "project_id": projection.project_id,
            "template_id": projection.template_id,
            **projection.content,
        }
        
        return template.render(context)

    def render_to_file(self, template_id: str, projection: Projection, output_path: Path, template_filename: str = "scroll.md.j2") -> Path:
        """Screenを指定された出力ファイルパスに書き出す"""
        rendered_content = self.render_to_string(template_id, projection, template_filename)
        
        # 出力先ディレクトリの確保
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 安全にファイルへ書き込み
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered_content)
            
        return output_path
