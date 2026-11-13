import os
import yaml

# [Chaos] 聖域の自動生成初期化ファイル
# 役割: 感覚器・揺らぎの原初インプット

CURRENT_ROOT = os.path.dirname(os.path.abspath(__file__))
REPOSITORY_ROOT = os.path.dirname(CURRENT_ROOT)
SANCTUARY_NAME = os.path.basename(CURRENT_ROOT)

def resolve_next_root():
    yml_path = os.path.join(REPOSITORY_ROOT, "architecture.yml")
    if os.path.exists(yml_path):
        try:
            with open(yml_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            for s in config.get("sanctuaries", []):
                if s["name"] == SANCTUARY_NAME:
                    next_name = s.get("next")
                    if next_name:
                        return os.path.join(REPOSITORY_ROOT, next_name)
        except Exception as e:
            print(f"⚠️ 読み込みエラー: {e}")
    return CURRENT_ROOT

SANCTUARY_ROOT = CURRENT_ROOT
NEXT_ROOT = resolve_next_root()
