import os
import cv2
import numpy as np

def calculate_color_histogram(image):
    histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    histogram = histogram.flatten()
    return histogram

def calculate_color_moments(image):
    moments = cv2.moments(image)
    color_moments = [moments['m00'], moments['m10'], moments['m01'], moments['m20'], moments['m11'], moments['m02']]
    return color_moments

def extract_dominant_color(image):
    pixels = image.reshape(-1, 3)
    pixel_counts = {}
    for pixel in pixels:
        pixel = tuple(pixel)
        pixel_counts[pixel] = pixel_counts.get(pixel, 0) + 1
    dominant_color = max(pixel_counts, key=pixel_counts.get)
    return dominant_color

def get_best_image(folder_path, sorting_method):
    image_files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    best_image_path = None
    best_property = None

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)

        if sorting_method == 'color_histogram':
            property_value = calculate_color_histogram(image)
        elif sorting_method == 'color_moments':
            property_value = calculate_color_moments(image)
        elif sorting_method == 'dominant_color':
            property_value = extract_dominant_color(image)

        if best_property is None or np.max(property_value) > np.max(best_property):
            best_property = property_value
            best_image_path = image_path

    if best_image_path:
        print("Best image:", os.path.basename(best_image_path))
        best_image = cv2.imread(best_image_path)
        cv2.namedWindow("Best Image", cv2.WINDOW_NORMAL)  # Set window to be resizable
        cv2.imshow("Best Image", best_image)
        cv2.waitKey(0)
    else:
        print("No images found in the folder.")

# Set the folder path and sorting method
folder_path = "C:/Users/ADMIN/Downloads/Youghurt and granola"
sorting_method = "color_histogram"  # Choose one: "color_histogram", "color_moments", "dominant_color"

get_best_image(folder_path, sorting_method)
