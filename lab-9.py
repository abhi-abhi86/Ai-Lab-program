import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def template_matching():
    # Placeholder paths - ensure files exist
    img_path = 'main_image.jpg'
    template_path = 'template.jpg'
    
    if not os.path.exists(img_path) or not os.path.exists(template_path):
        print("Images not found. Please provide 'main_image.jpg' and 'template.jpg'")
        return

    img = cv2.imread(img_path, 0) # Load as grayscale
    img2 = img.copy()
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]

    # List of comparison methods
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template matching
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
            
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(img, top_left, bottom_right, 255, 2)

        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.savefig('lab-9-output.png')
        print(f"Saved matching result for {meth} to lab-9-output.png")
        break # Just save one for the README
        # plt.show()

if __name__ == "__main__":
    print("Starting Template Matching...")
    template_matching()