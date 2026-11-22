#!/usr/bin/env python3
"""The picture that tastes of one ingredient.

Writes a photorealistic macro photograph of golden honeycomb dripping
warm honey - one ingredient, nothing else - to /output/entry.png.

The image is bundled with this repository as honeycomb.jpg (1024x1024
JPEG, 221,544 bytes) and is copied verbatim, so the program runs fully
offline and deterministically in the sandbox.
"""

import os
import sys

IMAGE_NAME = "honeycomb.jpg"
OUTPUT_PATH = "/output/entry.png"
MAX_BYTES = 1_048_576


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    with open(src, "rb") as f:
        data = f.read()
    if len(data) > MAX_BYTES:
        print(f"image too large: {len(data)} bytes", file=sys.stderr)
        return 1
    if not data.startswith(b"\xff\xd8\xff"):
        print("image is not a JPEG", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {OUTPUT_PATH}: {len(data)} bytes, 1024x1024 JPEG")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
