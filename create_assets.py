import cv2
import numpy as np

def create_smarties():
    # Create white image
    img = np.full((300, 300, 3), 255, dtype=np.uint8)
    # Draw some circles
    coords = [(50, 50), (150, 100), (250, 60), (100, 200), (200, 250)]
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 255, 255)] # BGR
    for (x, y), color in zip(coords, colors):
        cv2.circle(img, (x, y), 20, color, -1)
    
    cv2.imwrite('smarties.png', img)
    print("Created smarties.png")

def create_template_matching_images():
    # Create main image
    img = np.full((400, 400), 200, dtype=np.uint8) # Grey background
    # Add some meaningful pattern
    cv2.rectangle(img, (50, 50), (150, 150), 100, -1)
    cv2.circle(img, (300, 300), 50, 50, -1)
    
    # Specific bit to be the template
    cv2.rectangle(img, (200, 100), (250, 150), 0, -1) # Black box
    
    cv2.imwrite('main_image.jpg', img)
    
    # Create template (the black box)
    template = img[100:150, 200:250]
    cv2.imwrite('template.jpg', template)
    print("Created main_image.jpg and template.jpg")

if __name__ == "__main__":
    create_smarties()
    create_template_matching_images()
