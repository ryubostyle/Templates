import os
import yaml
from jinja2 import Template
from .film import Film

class BaseProjector:
    def __init__(self, template_path: str, output_path: str):
        self.template_path = template_path
        self.output_path = output_path

    def project(self, film_path: str) -> None:
        """ネガフィルムを読み込み、型枠を通してスクリーンへ投影する"""
        # 1. ネガフィルムの読み込み
        if not os.path.exists(film_path):
            raise FileNotFoundError(f"ネガフィルムが見つかりません: {film_path}")
        
        with open(film_path, "r", encoding="utf-8") as f:
            raw_data = yaml.safe_load(f) or {}
        
        film = Film.from_dict(raw_data)

        # 2. 型枠（テンプレート）の読み込み
        if not os.path.exists(self.template_path):
            raise FileNotFoundError(f"型枠テンプレートが見つかりません: {self.template_path}")

        with open(self.template_path, "r", encoding="utf-8") as f:
            template_content = f.read()

        # 3. 現像（レンダリング）の実行
        jinja_template = Template(template_content)
        rendered_content = jinja_template.render(
            film_id=film.film_id,
            title=film.title,
            source=film.source,
            latent_questions=film.latent_questions,
            provenance=film.provenance
        )

        # 4. スクリーン（出力先）への垂直投影
        output_dir = os.path.dirname(self.output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write(rendered_content)
        
        print(f"✨ [BaseProjector] 投影完了: {self.output_path} (from {film_path})")

