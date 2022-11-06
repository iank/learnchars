#!/usr/bin/env python
"""
Generate an image summary of learning progress for the N most frequent characters in
a format suitable for display on my KT2 kindle
"""
import sys
import argparse
from pathlib import Path
from learnchars.skritter import Skritter
from learnchars.chars import str_progress

from PIL import Image, ImageFont, ImageDraw


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Generate an image summary of learning progress')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    # Import vocabulary list
    vocab = Skritter(args.filename)
    (_, progress) = str_progress(vocab.chars, 1080, invert=False, line_width=40, border=False)

    font = ImageFont.truetype('simsun.ttc', 20)
    im = Image.new('L', (800, 600), 255)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), progress, font=font)
    del draw
    im.rotate(-90, expand=True).save(sys.stdout, "PNG")
