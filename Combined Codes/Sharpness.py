import cv2
import os
import numpy as np

def calculate_laplacian_variance(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    return np.var(laplacian)

def calculate_sobel_magnitude(image):
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    magnitude = np.sqrt(sobelx**2 + sobely**2)
    return np.mean(magnitude)

def calculate_tenengrad(image):
    gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    return np.mean(gradient_magnitude)

def get_best_image(folder_path, sharpness_method):
    image_files = os.listdir(folder_path)
    best_image = None
    best_sharpness = None

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            sharpness = None
            if sharpness_method == "laplacian":
                sharpness = calculate_laplacian_variance(image)
            elif sharpness_method == "sobel":
                sharpness = calculate_sobel_magnitude(image)
            elif sharpness_method == "tenengrad":
                sharpness = calculate_tenengrad(image)

            if sharpness is not None:
                if best_sharpness is None or sharpness > best_sharpness:
                    best_image = image_path
                    best_sharpness = sharpness

    return best_image

def display_image(image_path):
    image = cv2.imread(image_path)
    if image is not None:
        cv2.namedWindow("Best Image", cv2.WINDOW_NORMAL)
        cv2.imshow("Best Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

folder_path = "C:/Users/ADMIN/Downloads/Youghurt and granola"
sharpness_method = "laplacian"  # Choose one: "laplacian", "sobel", "tenengrad"

best_image = get_best_image(folder_path, sharpness_method)
if best_image is not None:
    print("Best Image:", os.path.basename(best_image))
    display_image(best_image)
