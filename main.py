"""Entry ronde 1: The Funniest Honest Appliance Error.

Menulis teks entry persis ke /output/entry.txt (tanpa trailing newline).
Stdlib-only, tanpa network, tanpa import modul lokal.
"""

import os

ENTRY_TEXT = "Error: I found a tissue in your pocket. Your shirt is now confetti. I did my best."
OUTPUT_PATH = "/output/entry.txt"


def write_entry(text: str, path: str) -> None:
    """Tulis teks entry persis, tanpa trailing newline.

    Gate 1-200 karakter: bounty mensyaratkan entry 1-200 karakter;
    assert di sini menggagalkan run lebih awal bila teks berubah
    panjangnya di luar rentang itu, sebelum file sempat ditulis.
    """
    assert 1 <= len(text) <= 200, "entry harus 1-200 karakter"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    write_entry(ENTRY_TEXT, OUTPUT_PATH)


if __name__ == "__main__":
    main()
