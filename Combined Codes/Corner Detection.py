import cv2
import os
import numpy as np

def get_best_image(folder_path, corner_method):
    best_image = None
    best_corners = 0

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            if corner_method == 'harris':
                corners = cv2.cornerHarris(gray, 2, 3, 0.04)
            elif corner_method == 'shi-tomasi':
                corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
            elif corner_method == 'fast':
                fast = cv2.FastFeatureDetector_create()
                keypoints = fast.detect(gray, None)
                corners = np.array([kp.pt for kp in keypoints], dtype=np.float32)

            if corners is not None and len(corners) > best_corners:
                best_corners = len(corners)
                best_image = image_path

    return best_image

def display_image(image_path):
    if image_path is not None:
        image_name = os.path.basename(image_path)
        print("Best Image:", image_name)
        image = cv2.imread(image_path)
        cv2.namedWindow(image_name, cv2.WINDOW_NORMAL)
        cv2.imshow(image_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Set the folder path and corner detection method
folder_path = "C:/Users/ADMIN/Downloads/Youghurt and granola"
corner_method = "harris"  # Choose one: "harris", "shi-tomasi", "fast"

# Get the best image based on corner detection
best_image = get_best_image(folder_path, corner_method)

# Display the best image in its original size and print the image name
display_image(best_image)
