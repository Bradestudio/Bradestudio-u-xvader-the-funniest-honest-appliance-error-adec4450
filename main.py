import os

ENTRY = "Error: I found a tissue in your pocket. Your shirt is now confetti. I did my best."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
