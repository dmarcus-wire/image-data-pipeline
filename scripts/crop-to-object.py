# USAGE
# python scripts/crop-to-object.py -i images/output/uss-freedom-original.jpg

# import necessary packages
import argparse
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str,
                help="path to input image")
args = vars(ap.parse_args())

# load, crop, save and show
image = cv2.imread(args["image"])
cropped = image[700:1050, 300:1400]
(h, w, c) = image.shape[:3]
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("channels: {}".format(c))
cv2.imshow("Cropped", cropped)
cv2.imwrite("images/output/uss-freedom-cropped.jpg", cropped)
cv2.waitKey(0)