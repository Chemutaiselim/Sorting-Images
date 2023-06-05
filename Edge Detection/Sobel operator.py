import cv2
import numpy as np

def calculate_rise_distance(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian smoothing to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Sobel operator to compute gradients
    gradient_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

    # Compute gradient magnitude and orientation
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
    gradient_orientation = np.arctan2(gradient_y, gradient_x)

    # Threshold the gradient magnitude
    _, thresholded = cv2.threshold(gradient_magnitude, 50, 255, cv2.THRESH_BINARY)

    # Perform dilation to connect broken edges (optional)
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(thresholded, kernel, iterations=1)

    # Find contours in the edge image
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    max_rise_distance = 0

    # Iterate over the contours
    for contour in contours:
        # Calculate the rise distance for each contour
        _, _, _, max_loc = cv2.minMaxLoc(gray, mask=np.uint8(thresholded == 255))
        _, _, _, min_loc = cv2.minMaxLoc(gray, mask=np.uint8(thresholded == 255), reverse=True)

        rise_distance = abs(max_loc[1] - min_loc[1])  # Calculate the rise distance

        if rise_distance > max_rise_distance:
            max_rise_distance = rise_distance

    return max_rise_distance

# Example usage
image_path = 'path/to/your/image.jpg'

# Load the image
image = cv2.imread(image_path)

# Calculate the rising distance using the Sobel operator
rising_distance = calculate_rise_distance(image)

print("Rising Distance:", rising_distance)
