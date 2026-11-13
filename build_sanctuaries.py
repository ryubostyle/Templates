import os
import yaml

def materialize_architecture():
    # 1. architecture.yml の読み込み
    yml_path = "architecture.yml"
    if not os.path.exists(yml_path):
        print("⚠️ architecture.yml が見つかりません。")
        return

    with open(yml_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    print("🏛️ [Auto-Builder] 宣言的アーキテクチャに基づく聖域の自動構築を開始します...")

    # 2. 各聖域のディレクトリと __init__.py の生成
    for sanctuary in config.get("sanctuaries", []):
        name = sanctuary["name"]
        role = sanctuary["role"]
        
        # フォルダの生成
        if not os.path.exists(name):
            os.makedirs(name)
            print(f"  + 📁 聖域フォルダ生成: {name}/")

        # .gitkeep の確保（空フォルダがgitに追跡されるようにする）
        gitkeep_path = os.path.join(name, ".gitkeep")
        if not os.path.exists(gitkeep_path):
            with open(gitkeep_path, 'w', encoding='utf-8') as gk:
                pass # 空ファイルとして生成

        # 各 __init__.py の自動動的記述
        init_path = os.path.join(name, "__init__.py")
        init_content = f'''import os
import yaml

# [{name}] 聖域の自動生成初期化ファイル
# 役割: {role}

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
            print(f"⚠️ 読み込みエラー: {{e}}")
    return CURRENT_ROOT

SANCTUARY_ROOT = CURRENT_ROOT
NEXT_ROOT = resolve_next_root()
'''

        with open(init_path, 'w', encoding='utf-8') as init_file:
            init_file.write(init_content)
        print(f"  + 📜 聖域の初期化定着: {name}/__init__.py")

    print("✨ [Auto-Builder] すべての聖域と動的トポロジの構築が完遂しました。")

if __name__ == "__main__":
    materialize_architecture()
