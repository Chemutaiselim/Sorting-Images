import cv2
import os
import numpy as np

def display_best_image_by_hue(folder_path, hue_method='hsv'):
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not image_files:
        print("No images found in the folder.")
        return

    hue_values = []
    images = []
    for image_file in image_files:
        image = cv2.imread(os.path.join(folder_path, image_file))
        if image is not None:
            hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            if hue_method == 'hsv':
                hue_channel = hsv_image[:, :, 0]
                hue = np.mean(hue_channel)
            elif hue_method == 'histogram':
                hist = cv2.calcHist([hsv_image], [0], None, [180], [0, 180])
                hue = np.argmax(hist)
            elif hue_method == 'kmeans':
                pixels = hsv_image.reshape((-1, 3)).astype(np.float32)
                criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
                _, _, centers = cv2.kmeans(pixels, 8, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
                hue_values = [c[0] for c in centers]
                hue = np.mean(hue_values)
            else:
                print("Invalid hue method.")
                return
            hue_values.append(hue)
            images.append(image)

    if not images:
        print("No valid images found in the folder.")
        return

    best_index = hue_values.index(max(hue_values))
    best_image = images[best_index]
    best_image_name = image_files[best_index]
    print("Best Image Name:", best_image_name)

    window_name = "Best Image (Hue: {})".format(hue_method.capitalize())
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, best_image.shape[1], best_image.shape[0])
    cv2.imshow(window_name, best_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
folder_path = "C:/Users/ADMIN/Downloads/Youghurt and granola"
display_best_image_by_hue(folder_path, hue_method='hsv')
