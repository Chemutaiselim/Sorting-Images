import cv2
import os
import numpy as np

def apply_histogram_equalization(image):
    return cv2.equalizeHist(image)

def apply_clahe(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(image)

def apply_retinex(image):
    scales = [15, 80, 250]
    retinex_image = np.zeros_like(image)
    for scale in scales:
        blur = cv2.GaussianBlur(image, (scale, scale), 0)
        retinex = np.log10(image + 1) - np.log10(blur + 1)
        retinex_image = np.maximum(retinex_image, retinex)
    return cv2.normalize(retinex_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

def calculate_contrast_stddev(image):
    _, stddev = cv2.meanStdDev(image)
    return stddev[0, 0]

def get_best_image(folder_path, contrast_method):
    image_files = os.listdir(folder_path)
    best_image = None
    best_contrast = None

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            processed_image = None
            if contrast_method == "histogram_equalization":
                processed_image = apply_histogram_equalization(image)
            elif contrast_method == "clahe":
                processed_image = apply_clahe(image)
            elif contrast_method == "retinex":
                processed_image = apply_retinex(image)

            if processed_image is not None:
                contrast = calculate_contrast_stddev(processed_image)
                if best_contrast is None or contrast > best_contrast:
                    best_image = image_path
                    best_contrast = contrast

    return best_image

def display_image(image_path):
    image = cv2.imread(image_path)
    if image is not None:
        cv2.namedWindow("Best Image", cv2.WINDOW_NORMAL)
        cv2.imshow("Best Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

folder_path = "C:/Users/ADMIN/Downloads/Youghurt and granola"
contrast_method = "histogram_equalization"  # Choose one: "histogram_equalization", "clahe", "retinex"

best_image = get_best_image(folder_path, contrast_method)
if best_image is not None:
    print("Best Image:", os.path.basename(best_image))
    display_image(best_image)
