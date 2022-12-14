import numpy as np
import pillow_heif
from PIL import Image
import sys
import cv2

def main():
    param = sys.argv
    original_image = Image.open(param[1])
    original_image = np.array(original_image)
    heif_image = pillow_heif.open_heif(param[2])
    heif_image = np.array(heif_image)
    png = cv2.imread(param[3])

    canny_image = cv2.Canny(png, 100, 200)
    cv2.imshow("cannyimage", canny_image)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()