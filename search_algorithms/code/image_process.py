import cv2 as cv
import numpy as np

def load_image(fileName: str):
    """
    Read and load an image in grayscale
    """
    # read image in grayscale
    gray_img = cv.imread(fileName, cv.IMREAD_GRAYSCALE)
    
    return gray_img

def binarize_image(img, threshold: int=100, maxVal: int=255):
    """
    Perform the binary thresholding process to each pixel of the image.

    Parameters
    ----------
    * `img`: a mat as returned by `cv2.imread()`
    """
    _, bin_img = cv.threshold(img, threshold, maxVal, cv.THRESH_BINARY)
    
    return bin_img

def display(windowName: str, img):
    cv.imshow(windowName, img)
    cv.waitKey(0)