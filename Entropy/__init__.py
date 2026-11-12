# Entropy/__init__.py
import os

ENTROPY_ROOT = os.path.dirname(os.path.abspath(__file__))
REPOSITORY_ROOT = os.path.dirname(ENTROPY_ROOT)
PROCESSOR_ROOT = os.path.join(REPOSITORY_ROOT, "Processor")

print(f"  - ⚡ [Entropy Sanctuary Initialized] 零点座標: {ENTROPY_ROOT}")
