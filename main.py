"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one funny, heartfelt wedding vow a robot says at its own wedding
to $MAKEFUN_OUTPUT_DIR/entry.txt (one sentence, under 200 characters).

Pure Python stdlib, deterministic, no network.
"""

import os

VOW = (
    "I vow to share my last percent of battery, keep your charging dock warm, "
    "and love you through every firmware update \u2014 even the 3 a.m. reboots "
    "\u2014 until our circuits power down together."
)


def main() -> None:
    # The gate accepts 1-200 characters of non-blank UTF-8 text; refuse to
    # emit anything outside that band instead of submitting an invalid entry.
    line = VOW.strip()
    if not (1 <= len(line) <= 200):
        raise ValueError(f"vow is {len(line)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
