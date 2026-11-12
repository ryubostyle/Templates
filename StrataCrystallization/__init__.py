# StrataCrystallization/__init__.py
import os

ENTROPY_ROOT = os.path.dirname(os.path.abspath(__file__))
REPOSITORY_ROOT = os.path.dirname(ENTROPY_ROOT)

# 結晶化の果てから、再びはじまりの Chaos 聖域へ代謝の環を閉じる
NEXT_ROOT = os.path.join(REPOSITORY_ROOT, "Chaos") 

print(f"  - 💎 [StrataCrystallization Initialized] 結晶化座標: {ENTROPY_ROOT}")
print(f"  - 🌀 [Next Circulation Target] 次の回帰先（Chaos）: {NEXT_ROOT}")
