#!/usr/bin/env python3
"""
Question 1 – Custom two-parameter shift cipher (asymmetric rules).
"""
from pathlib import Path

RAW_FILE = Path("raw_text.txt")
ENC_FILE = Path("encrypted_text.txt")
DEC_FILE = Path("decrypted_text.txt")
ALPH_LO = "abcdefghijklmnopqrstuvwxyz"
ALPH_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def _shift_char(c: str, shift: int, alphabet: str) -> str:
    i = alphabet.find(c)
    if i == -1: return c
    return alphabet[(i + shift) % len(alphabet)]

def encrypt_char(c: str, s1: int, s2: int) -> str:
    if c.islower() and c in ALPH_LO:
        if c <= 'm':
            return _shift_char(c, s1 * s2, ALPH_LO)
        else:
            return _shift_char(c, -(s1 + s2), ALPH_LO)
    elif c.isupper() and c in ALPH_UP:
        if c <= 'M':
            return _shift_char(c, -s1, ALPH_UP)
        else:
            return _shift_char(c, s2 ** 2, ALPH_UP)
    else:
        return c

def decrypt_char(c: str, s1: int, s2: int) -> str:
    for guess in ALPH_LO + ALPH_UP:
        if encrypt_char(guess, s1, s2) == c:
            return guess
    return c

def main():
    try:
        s1 = int(input("Enter shift1 (integer): ").strip())
        s2 = int(input("Enter shift2 (integer): ").strip())
    except ValueError:
        print("Error: integers required."); return

    if not RAW_FILE.exists():
        RAW_FILE.write_text("Sample text for Q1. Replace with your own.\n", encoding="utf-8")
        print("Created sample raw_text.txt. Re-run the program."); return

    raw = RAW_FILE.read_text(encoding="utf-8")
    enc = "".join(encrypt_char(ch, s1, s2) for ch in raw)
    ENC_FILE.write_text(enc, encoding="utf-8")
    dec = "".join(decrypt_char(ch, s1, s2) for ch in enc)
    DEC_FILE.write_text(dec, encoding="utf-8")
    print("Decryption verification:", "SUCCESS ✅" if raw == dec else "FAILED ❌")

if __name__ == "__main__":
    main()
