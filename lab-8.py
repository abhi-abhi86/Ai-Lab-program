import cv2
import numpy as np
import sys

def main():
    # Load image (Use a placeholder filename or provide a path)
    filename = 'assets/smarties.png' # Example filename
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    src = cv2.imread(filename, cv2.IMREAD_COLOR)
    
    if src is None:
        print("Error opening image!")
        return
        
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    # Blur to reduce noise
    gray = cv2.medianBlur(gray, 5)
    
    rows = gray.shape[0]
    
    # Apply Hough Circle Transform
    circles = cv2.HoughCircles(
        gray, 
        cv2.HOUGH_GRADIENT, 
        dp=1, 
        minDist=rows/8,
        param1=100, 
        param2=30, 
        minRadius=1, 
        maxRadius=30
    )
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # Circle center
            cv2.circle(src, center, 1, (0, 100, 100), 3)
            # Circle outline
            radius = i[2]
            cv2.circle(src, center, radius, (255, 0, 255), 3)
            
    cv2.imshow("detected circles", src)
    # cv2.imwrite("lab-8-output.png", src)
    print("Displayed output in window")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Note: This requires an actual image file to run locally
    print("Running Hough Circle detection (Requires 'smarties.png' or argument)")
    main()