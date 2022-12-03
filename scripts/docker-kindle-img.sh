#!/bin/bash

# Script for the docker image to update vocabulary list and generate kindle images
source /venv/bin/activate

skritter_dl $SKRITTER_USERNAME $SKRITTER_PW > /data/skritter.tsv
kindle_img /data/skritter.tsv > /data/bg_ss00.png
kindle_img /data/skritter.tsv -i > /data/bg_ss01.png
