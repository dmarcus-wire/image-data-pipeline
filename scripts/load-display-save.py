# USAGE
# python scripts/load-display-save.py -i images/input/uss-freedom.jpg

# import necessary packages
import argparse
import imutils
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, default="./images/input/uss-freedom.jpg", # single switch image path to image on disk
                help="path to input image")
args = vars(ap.parse_args())

# load, dimensions, display and save
image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("channels: {}".format(c))
cv2.imshow("Image", image)
cv2.imwrite("images/output/uss-freedom-original.jpg", image)
cv2.waitKey(0)