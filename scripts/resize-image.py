# USAGE
# python scripts/resize-image.py -i images/output/uss-freedom-cropped.jpg

# import necessary packages
import argparse
import imutils
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, # single switch image path to image on disk
                help="path to input image")
args = vars(ap.parse_args())

# load, , calculate aspect ratio, resize, dimensions, display and save
image = cv2.imread(args["image"])
resized = imutils.resize(image, width=300)
(h, w, c) = resized.shape[:3]
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("channels: {}".format(c))
cv2.imshow("Resized using imutils", resized)
cv2.imwrite("images/output/uss-freedom-resized.jpg", resized)
cv2.waitKey(0)