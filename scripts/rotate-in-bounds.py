# USAGE
# python scripts/rotate-in-bounds.py -i images/output/uss-freedom-cropped.jpg

# import necessary packages
import argparse
import imutils
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, # single switch image path to image on disk
                help="path to input image")
args = vars(ap.parse_args())

# load and display original
image = cv2.imread(args["image"]) # load image from disk
cv2.imshow("Original", image)

# rotate and save
rotate33cc = imutils.rotate_bound(image, -33) # rotate in bounds
cv2.imshow("Rotated without cropping", rotate33cc)
cv2.imwrite("images/output/uss-freedom-rotate-33cc.jpg", rotate33cc)
cv2.waitKey(0)

rotate45c = imutils.rotate_bound(image, 45) # rotate in bounds
cv2.imshow("Rotated without cropping", rotate45c)
cv2.imwrite("images/output/uss-freedom-rotate-45c.jpg", rotate45c)
cv2.waitKey(0)

rotate90cc = imutils.rotate_bound(image, -90) # rotate in bounds
cv2.imshow("Rotated without cropping", rotate90cc)
cv2.imwrite("images/output/uss-freedom-rotate-90cc.jpg", rotate90cc)
cv2.waitKey(0)

rotate180c = imutils.rotate_bound(image, -33) # rotate in bounds
cv2.imshow("Rotated without cropping", rotate180c)
cv2.imwrite("images/output/uss-freedom-rotate-180c.jpg", rotate180c)
cv2.waitKey(0)