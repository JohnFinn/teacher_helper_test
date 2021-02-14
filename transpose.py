#!/usr/bin/env python3
import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1])
cv2.imwrite(sys.argv[2], np.transpose(img, axes=(1,0,2)))