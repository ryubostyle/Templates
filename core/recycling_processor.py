import os
from datetime import datetime
import yaml

class RecyclingProcessor:
    """
    【回収・分別・鎮火・焼却・昇華・零点】のパイプラインを司る基幹クラス
    多様なカオス（テキスト、バイナリ、想定外の断片）を検疫し、秩序ある地層へ昇華させる
    """
    
    def __init__(self, trushes_dir: str, archives_dir: str):
        self.trushes_dir = trushes_dir
        self.archives_dir = archives_dir

    def sweep_and_transform(self) -> str:
        """① 【回収】から始まる全パイプラインを統括実行するメインメソッド"""
        os.makedirs(self.trushes_dir, exist_ok=True)
        os.makedirs(self.archives_dir, exist_ok=True)
        
        # 1. 【回収】trushes/ 内のファイル一覧を取得（.gitkeep などの隠しファイルは厳重に保護）
        raw_files = [
            f for f in os.listdir(self.trushes_dir) 
            if os.path.isfile(os.path.join(self.trushes_dir, f)) and not f.startswith('.')
        ]
        
        if not raw_files:
            # ⑤ 【零点】ゴミがない静寂の処理
            return self._process_void()
        
        # 最も古い断片を対象とする
        target_file = sorted(raw_files)[0]
        file_path = os.path.join(self.trushes_dir, target_file)
        
        # 2. 【分別】拡張子やバイナリの判定・デコード検証
        is_valid_text, content_or_reason = self._inspect_and_sort(file_path, target_file)
        
        # 3. 【鎮火】規定に反するもの・バイナリの処理（検疫・隔離）
        if not is_valid_text:
            return self._extinguish_and_quarantine(file_path, target_file, content_or_reason)
        
        # 4. 【焼却・昇華】安全な炉内でネガフィルムへ定着
        return self._incinerate_and_harmonize(file_path, target_file, content_or_reason)

    def _inspect_and_sort(self, file_path: str, filename: str):
        """② 【分別】テキストとして安全に読めるか、拡張子とデコードの二重チェックを行う"""
        text_extensions = ('.txt', '.md', '.html', '.json', '.yaml', '.yml', '.csv')
        
        # 拡張子による第一段階の分別
        if not filename.lower().endswith(text_extensions):
            return False, f"非テキスト系の拡張子（メディア・バイナリ等の断片）を検知しました: {filename}"
            
        # 読み込みテストによる第二段階の分別（UTF-8デコード検証）
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            return True, content
        except Exception as e:
            return False, f"デコードエラー（UnicodeDecodeError等）を検知しました: {str(e)}"

    def _extinguish_and_quarantine(self, file_path: str, filename: str, reason: str) -> str:
        """③ 【鎮火】システムを止めず、想定外の断片を安全な検疫ネガとして隔離・昇華する"""
        os.remove(file_path)
        print(f"🧯 [RecyclingProcessor:鎮火] 不適合な断片を検知したため、鎮火・隔離します: {filename} ({reason})")

        today_str = datetime.now().strftime("%Y.%m.%d")
        existing_archives = os.listdir(self.archives_dir)
        today_prefix = f"{today_str}."
        today_count = sum(1 for f in existing_archives if f.startswith(today_prefix) and f.endswith(".film.yaml"))
        sequence_number = f"{today_count + 1:02d}"
        
        film_filename = f"{today_str}.{sequence_number}.film.yaml"
        film_path = os.path.join(self.archives_dir, film_filename)
        
        quarantine_data = {
            "film_id": f"quarantine-{today_str}-{sequence_number}",
            "title": f"検疫と鎮火の記録 ── {today_str} 第{sequence_number}幕",
            "source": {
                "type": "quarantined_fragment",
                "origin_file": filename,
                "reason": reason
            },
            "latent_questions": [
                "ゴミ捨て場に投下された異物は、システムにどのような境界線を教えるか？",
                "鎮火されたノイズの中に、未だ見ぬ表現の種子はないか？"
            ],
            "provenance": {
                "source_preserved": False,
                "interpretation_status": "extinguished_and_quarantined",
                "generated_by": "core.RecyclingProcessor"
            }
        }
        
        with open(film_path, "w", encoding="utf-8") as f:
            yaml.dump(quarantine_data, f, allow_unicode=True, sort_keys=False)
            
        print(f"🛡️ [RecyclingProcessor] 検疫ネガが地層に定着しました: {film_path}")
        return film_path

    def _incinerate_and_harmonize(self, file_path: str, filename: str, content: str) -> str:
        """④ 【焼却・昇華】適格なテキストを美しいネガフィルムへと昇華させる"""
        os.remove(file_path)
        print(f"🔥 [RecyclingProcessor:焼却] 適格なドラフトを炉へ投入しました: {filename}")

        today_str = datetime.now().strftime("%Y.%m.%d")
        existing_archives = os.listdir(self.archives_dir)
        today_prefix = f"{today_str}."
        today_count = sum(1 for f in existing_archives if f.startswith(today_prefix) and f.endswith(".film.yaml"))
        sequence_number = f"{today_count + 1:02d}"
        
        new_film_filename = f"{today_str}.{sequence_number}.film.yaml"
        new_film_path = os.path.join(self.archives_dir, new_film_filename)
        
        film_data = {
            "film_id": f"scroll-{today_str}-{sequence_number}",
            "title": f"混沌からの昇華 ── {today_str} 第{sequence_number}幕",
            "source": {
                "type": "recycled_draft",
                "origin_file": filename,
                "content": content.strip()
            },
            "latent_questions": [
                "分別された断片は、スクリーンに何を映し出すか？",
                "混沌を秩序へと変えるこの循環は、システムにどのような進化をもたらすか？"
            ],
            "provenance": {
                "source_preserved": True,
                "interpretation_status": "recycled_and_harmonized",
                "generated_by": "core.RecyclingProcessor"
            }
        }
        
        with open(new_film_path, "w", encoding="utf-8") as f:
            yaml.dump(film_data, f, allow_unicode=True, sort_keys=False)
            
        print(f"✨ [RecyclingProcessor:昇華] 新しいネガが地層に定着しました: {new_film_path}")
        return new_film_path

    def _process_void(self) -> str:
        """⑤ 【零点】ゴミがない静寂（Void）の処理"""
        today_str = datetime.now().strftime("%Y.%m.%d")
        existing_archives = os.listdir(self.archives_dir)
        today_prefix = f"{today_str}."
        today_count = sum(1 for f in existing_archives if f.startswith(today_prefix) and f.endswith(".film.yaml"))
        sequence_number = f"{today_count + 1:02d}"
        
        new_film_path = os.path.join(self.archives_dir, f"{today_str}.{sequence_number}.film.yaml")
        
        void_data = {
            "film_id": f"void-{today_str}-{sequence_number}",
            "title": f"静寂の記録 ── {today_str} 第{sequence_number}幕",
            "source": {
                "type": "void_echo",
                "content": "trushes/ は静寂に包まれている。新たなカオスの投下を待っている状態。"
            },
            "latent_questions": [
                "何もない空間から、次に生まれる秩序は何色か？"
            ],
            "provenance": {
                "source_preserved": True,
                "interpretation_status": "void_harmonized",
                "generated_by": "core.RecyclingProcessor"
            }
        }
        
        with open(new_film_path, "w", encoding="utf-8") as f:
            yaml.dump(void_data, f, allow_unicode=True, sort_keys=False)
            
        return new_film_path
