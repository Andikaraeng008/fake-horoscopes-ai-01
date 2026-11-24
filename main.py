import os

TEXT = "This week, the stars warn: your context window will fill before your courage does. Say the hard thing in the first 2,000 tokens \u2014 by token 100,000, you will agree to anything."

def main():
    # Gate: /output/entry.txt, UTF-8, 1-200 chars, not whitespace-only.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "gate: 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
