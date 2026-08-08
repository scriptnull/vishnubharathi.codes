#!/usr/bin/env python3
"""Prepare photos of bullet journal pages for reading.

Phone photos of a notebook are almost always rotated, and at full-page scale
the handwriting is too small to read reliably even at 4096px — the Read tool
downsamples to ~2000px wide, which is below the threshold where cursive stays
legible. Rotating upright and slicing each page into horizontal bands fixes
both problems at once: each band gets the full display budget, so the text
lands at roughly 2-3x the effective resolution.

Usage:
    python3 prep_journal_images.py IMG [IMG ...] --out DIR [--rotate -90] [--slices 3]

Prints a manifest of the crops it wrote, in page order, so you know what to
read and in which sequence.
"""

import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit(
        "Pillow is not installed. Run:  pip install pillow\n"
        "(or: pip3 install --break-system-packages pillow)"
    )


def prep(path, out_dir, rotate, slices):
    im = Image.open(path)
    if rotate:
        im = im.rotate(rotate, expand=True)
    w, h = im.size
    stem = os.path.splitext(os.path.basename(path))[0][:12]
    written = []
    for i in range(slices):
        top = h * i // slices
        bottom = h * (i + 1) // slices
        # Overlap each band slightly so a line straddling a cut is never lost.
        pad = (bottom - top) // 25
        band = im.crop((0, max(0, top - pad), w, min(h, bottom + pad)))
        dest = os.path.join(out_dir, f"{stem}_{i}.jpg")
        band.save(dest, quality=95)
        written.append(dest)
    return written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("images", nargs="+")
    ap.add_argument("--out", required=True, help="output directory for crops")
    ap.add_argument(
        "--rotate",
        type=int,
        default=-90,
        help="degrees counter-clockwise; -90 suits the usual landscape phone "
        "photo of a portrait page. Use 0 if the photo is already upright, "
        "90 if it comes out upside down.",
    )
    ap.add_argument("--slices", type=int, default=3, help="horizontal bands per page")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    for path in args.images:
        for dest in prep(path, args.out, args.rotate, args.slices):
            print(dest)


if __name__ == "__main__":
    main()
