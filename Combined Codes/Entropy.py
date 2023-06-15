import cv2
import os
import numpy as np

def display_best_image_by_entropy(folder_path, entropy_method='shannon'):
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not image_files:
        print("No images found in the folder.")
        return

    entropy_values = []
    images = []
    for image_file in image_files:
        image = cv2.imread(os.path.join(folder_path, image_file))
        if image is not None:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            if entropy_method == 'shannon':
                entropy = -np.sum(np.multiply(np.log2(np.clip(cv2.calcHist([gray_image], [0], None, [256], [0, 256]) / gray_image.size, 1e-10, 1)),
                                              cv2.calcHist([gray_image], [0], None, [256], [0, 256]) / gray_image.size))
            elif entropy_method == 'tsallis':
                entropy = 1 - np.sum(np.power(np.clip(cv2.calcHist([gray_image], [0], None, [256], [0, 256]) / gray_image.size, 1e-10, 1), 2))
            elif entropy_method == 'renyi':
                alpha = 2  # You can adjust the alpha value for Renyi entropy
                entropy = 1 / (1 - alpha) * np.log(np.sum(np.power(np.clip(cv2.calcHist([gray_image], [0], None, [256], [0, 256]) / gray_image.size, 1e-10, 1), alpha)))
            else:
                print("Invalid entropy method.")
                return
            entropy_values.append(entropy)
            images.append(image)

    if not images:
        print("No valid images found in the folder.")
        return

    best_index = entropy_values.index(max(entropy_values))
    best_image = images[best_index]
    best_image_name = image_files[best_index]
    print("Best Image Name:", best_image_name)

    window_name = "Best Image (Entropy: {})".format(entropy_method.capitalize())
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, best_image.shape[1], best_image.shape[0])
    cv2.imshow(window_name, best_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
folder_path = "C:/Users/ADMIN/Downloads/Youghurt and granola"
display_best_image_by_entropy(folder_path, entropy_method='shannon')
