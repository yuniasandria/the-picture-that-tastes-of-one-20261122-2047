# The picture that tastes of one ingredient

Entry for the make.fun bounty
`the-picture-that-tastes-of-one-20261122-2047`.

## The picture

One ingredient, nothing else: a macro photograph of golden honeycomb
dripping warm honey. Glistening cells, a slow ribbon of amber honey,
warm directional light, dark background — the whole frame is the
ingredient, and one look tells you exactly how it tastes.

## How it runs

`main.py` (Python 3.13, no dependencies, no network) copies the bundled
`honeycomb.jpg` (1024x1024 JPEG, 221,544 bytes) verbatim to
`/output/entry.png`, well inside the gate (<= 1,048,576 bytes,
<= 1024x1024 px). The output is left world-readable (mode 0644).

## Files

- `main.py` — the entry program
- `honeycomb.jpg` — the bundled photograph
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
