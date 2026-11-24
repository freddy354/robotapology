"""The Robot Apology: a robot apologises for a mistake it made, in its own voice.

Gate: the apology must be 1-400 characters long and exactly 2 lines.
"""

MAX_LEN = 400

TEXT = (
    "I watered the plastic fern on your desk for eleven days and let the real fern die.\n"
    "I will check for soil before pouring, because water entering without exit was the only signal I ignored."
)

# Gate check: entry must fit the 1-400 character limit (MAX_LEN = 400).
# Failing here stops the run before any file is written, so a too-long
# apology can never produce a stale or invalid entry.txt.
assert len(TEXT) <= MAX_LEN, f"text too long: {len(TEXT)} > {MAX_LEN}"

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = "./output/entry.txt"


def main():
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)
        path = OUTPUT_PATH
    except OSError:
        import os

        os.makedirs("./output", exist_ok=True)
        with open(FALLBACK_PATH, "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)
        path = FALLBACK_PATH

    # Read-back self-check: file must be byte-identical to TEXT.
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    assert content == TEXT, "read-back mismatch: entry.txt does not match TEXT"
    print(f"wrote {path} ({len(TEXT)} chars)")


if __name__ == "__main__":
    main()
