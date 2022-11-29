#!/usr/bin/env python
"""
Generate an image summary of learning progress for the N most frequent characters in
a format suitable for display on my KT2 kindle
"""
import sys
import os
import argparse
from pathlib import Path
from learnchars.skritter import Skritter
from learnchars.chars import str_progress

from PIL import Image, ImageFont, ImageDraw

FONT_FILE = 'simsun.ttc'

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Generate an image summary of learning progress')
    p.add_argument('filename', type=Path, metavar='filename.tsv', help='path to Skritter tsv')
    p.add_argument('-i', '--invert', action='store_true', help='display unknown characters')
    args = p.parse_args()

    if not args.filename.is_file():
        sys.exit("Path to vocabulary list does not exist or is not a file")

    if not os.path.isfile(FONT_FILE):
        sys.exit(f"Please download {FONT_FILE} and place it in this directory")

    # Import vocabulary list
    vocab = Skritter(args.filename)
    (_, progress) = str_progress(
        vocab.chars, 1080, invert=args.invert, line_width=40, border=False)

    font = ImageFont.truetype(FONT_FILE, 20)
    im = Image.new('L', (800, 600), 255)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), progress, font=font)
    del draw
    im.rotate(-90, expand=True).save(sys.stdout, "PNG")
