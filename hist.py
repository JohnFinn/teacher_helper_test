#!/usr/bin/env python3

import cv2
import numpy as np
import sys
from operator import itemgetter

img = cv2.imread(sys.argv[1])

freqs = {}
for pixel in img.reshape((-1, 3)):
    pixel = tuple(pixel)
    freqs[pixel] = freqs.get(pixel, 0) + 1

for (r, g, b), freq in sorted(freqs.items(), key=itemgetter(1), reverse=True):
    print(f'{r:3} {g:3} {b:3}: {freq}')
