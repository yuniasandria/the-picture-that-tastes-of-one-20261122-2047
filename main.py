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


def check_jpeg_bytes(data: bytes) -> bool:
    """True when data looks like a JPEG that fits the entry cap."""
    if not data:
        print("image is empty", file=sys.stderr)
        return False
    if len(data) > MAX_BYTES:
        print(f"image exceeds the cap: {len(data)} bytes", file=sys.stderr)
        return False
    if data[:3] != b"\xff\xd8\xff":
        print("image lacks the JPEG magic bytes", file=sys.stderr)
        return False
    return True


def save_entry_png(data: bytes) -> None:
    """Write the entry image to OUTPUT_PATH with mode 0644."""
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as out:
        out.write(data)
    os.chmod(OUTPUT_PATH, 0o644)


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(src):
        print(f"missing image: {src}", file=sys.stderr)
        return 1
    if os.path.getsize(src) > MAX_BYTES:
        print(f"image exceeds the cap before reading: {src}", file=sys.stderr)
        return 1
    with open(src, "rb") as f:
        data = f.read()
    if not check_jpeg_bytes(data):
        return 1
    save_entry_png(data)
    print(f"wrote {OUTPUT_PATH}: {len(data)} bytes, 1024x1024 JPEG")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
