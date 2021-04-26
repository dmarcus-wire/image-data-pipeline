# USAGE
# python scripts/image-arithmetic.py -i images/output/uss-freedom-rotate-90cc.jpg

# import necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, # single switch image path to image on disk
                help="path to input image")
args = vars(ap.parse_args())

# load and display original
image = cv2.imread(args["image"]) # load image from disk
cv2.imshow("Original", image)

# lighten, save
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Lighter", added)
cv2.imwrite("images/output/uss-freedom-rotate-90cc-lt.jpg", added)

# darken, save
M = np.ones(image.shape, dtype="uint8") * 70
subtracted = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted)
cv2.imwrite("images/output/uss-freedom-rotate-90cc-dk.jpg", subtracted)
cv2.waitKey(0)