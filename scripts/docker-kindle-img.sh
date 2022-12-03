#!/bin/bash

# Script for the docker image to update vocabulary list and generate kindle images
source /venv/bin/activate

skritter_dl $SKRITTER_USERNAME $SKRITTER_PW > /app/skritter.tsv
kindle_img /app/skritter.tsv > /app/bg_ss00.png
kindle_img /app/skritter.tsv -i > /app/bg_ss01.png
