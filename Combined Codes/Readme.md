# 1. Hue Sorting
Hue represents the dominant color wavelength in an image and can be useful for various purposes such as image analysis, color-based retrieval, or artistic filtering.

## Available Sorting Methods

1. **HSV Sorting**: Calculates the average hue value of each image using the HSV color space and sorts them accordingly.
2. **Hue Histogram Sorting**: Builds a histogram of the hue channel in the HSV color space to determine the dominant hue, and then sorts the images based on this information.
3. **K-means Clustering**: Applies K-means clustering to group the pixels of each image based on their hue values. The average hue of the resulting clusters is calculated, and the images are sorted accordingly.

## Usage

1. Prepare a folder containing the images to be sorted.
2. Set the folder path in the code.
3. Choose the desired sorting method by specifying it in the code by passing corresponding string parameter to the hue_method argument.
4. Run the code to display the best image based on the selected hue sorting method.

## How code works 
1. `calculate_average_hue(image)`: Calculates the average hue value of an image using the HSV color space.
2. `calculate_hue_histogram(image)`: Builds a histogram of the hue channel in the HSV color space.
3. `perform_kmeans_clustering(image)`: Applies K-means clustering to group the pixels of an image based on their hue values.
4. `get_best_image(folder_path, sorting_method)`: Determines the best image with the highest hue value.
5. `display_image(image_path)`: Loads and displays the image.


# 2. Entropy Sorting

The Entropy Sorting feature allows you to sort images in a folder based on their entropy properties. Entropy measures the randomness or complexity of an image and can be useful for tasks such as image quality assessment, feature extraction, or content analysis.

## Available Sorting Methods

1. **Shannon Entropy Sorting**: Sorts images based on the Shannon entropy, which quantifies the average amount of information or uncertainty in an image.
2. **Tsallis Entropy Sorting**: Sorts images based on the Tsallis entropy, which is a generalized form of entropy that considers the statistical distribution of pixel intensities.
3. **Renyi Entropy Sorting**: Sorts images based on the Renyi entropy, which provides a generalized measure of image complexity and can capture different aspects of the image distribution.

## How Code Works
1. The code calculates the entropy value for each valid image in the folder and stores them in the entropy_values list.
2. The image with the highest entropy is determined by finding the maximum value in the entropy_values list and retrieving its index.
3. The best image path is constructed using the folder path and the image file name from the image_files list.
Finally, the best image is loaded and displayed using OpenCV's cv2.imshow() function.


# 3. Color Sorting
Color sorting allows you to find and display the best image in a folder based on various color properties. Different color sorting methods can provide insights into color composition, distribution, or dominant colors in an image.

## Available Sorting Methods
1. Color Histogram Sorting: Sorts images based on their color histograms, which represent the distribution of color values in an image.
2. Color Moments Sorting: Sorts images based on color moments, which capture statistical properties of color distribution, such as mean, standard deviation, and skewness.
3. Dominant Color Extraction: Sorts images based on their dominant colors, which are the most prevalent or representative colors in an image.

## How Code Works
1. `calculate_color_histogram(image)`: Calculates the color histogram for an image, representing the distribution of color values.
2. `calculate_color_moments(image)`: Computes color moments for an image, capturing statistical properties of color distribution.
3. `extract_dominant_color(image)`: Extracts the dominant color from an image, representing the most prevalent or representative color.
4. `get_best_image(folder_path, sorting_method)`: Determines the best image with the highest color property based on the chosen sorting method.
5. `display_image(image_path)` Loads and displays the image in its original size.


# 4. Contrast Sorting

The Contrast Sorting feature allows you to sort images in a folder based on their contrast properties. Contrast refers to the difference in brightness between the light and dark areas of an image, and it plays an important role in image analysis, enhancement, and visual perception.

## Available Sorting Methods

1. **Histogram Equalization**: Enhances the contrast of an image by redistributing pixel intensities.
2. **Contrast Limited Adaptive Histogram Equalization (CLAHE)**: Improves contrast while limiting amplification in noise regions.
3. **Retinex-based Algorithms**: Applies multi-scale Retinex algorithms to enhance contrast by removing the illumination component.

## Usage

1. Prepare a folder containing the images to be sorted.
2. Set the folder path in the code.
3. Choose the desired contrast sorting method by specifying it in the code using the `contrast_method` parameter.
4. Run the code to display the best image based on the selected contrast sorting method.

## How Code Works

1. `apply_histogram_equalization(image)`: Applies histogram equalization to enhance the contrast of the image.
2. `apply_clahe(image)`: Applies Contrast Limited Adaptive Histogram Equalization (CLAHE) to improve contrast while limiting amplification in noise regions.
3. `apply_retinex(image)`: Applies multi-scale Retinex algorithms to enhance contrast by removing the illumination component.
4. `calculate_contrast_stddev(image)`: Calculates the contrast of an image using the standard deviation of pixel intensities.
5. `get_best_image(folder_path, contrast_method)`: Determines the best image with the highest contrast using the specified contrast sorting method.
6. `display_image(image_path)`: Loads and displays the image.


# 5. Sharpness Sorting

The Sharpness Sorting feature allows you to sort images in a folder based on their sharpness properties. Sharpness refers to the clarity and focus of an image, and it plays a crucial role in various image analysis tasks such as image quality assessment, object detection, and image enhancement.

## Available Sorting Methods

1. **Laplacian Filter**: Calculates the variance of the Laplacian response to measure the sharpness of an image.
2. **Sobel Operator**: Computes the gradient magnitude using the Sobel operator to estimate the image sharpness.
3. **Tenengrad (Gradient Magnitude)**: Evaluates the sharpness by calculating the average gradient magnitude using the Tenengrad algorithm.

## Usage

1. Prepare a folder containing the images to be sorted.
2. Set the folder path in the code.
3. Choose the desired sharpness sorting method by specifying it in the code using the `sharpness_method` parameter.
4. Run the code to display the best image based on the selected sharpness sorting method.

## How Code Works

1. `calculate_laplacian_variance(image)`: Calculates the variance of the Laplacian response to measure the sharpness of an image.
2. `calculate_sobel_magnitude(image)`: Computes the gradient magnitude using the Sobel operator to estimate the image sharpness.
3. `calculate_tenengrad(image)`: Evaluates the sharpness by calculating the average gradient magnitude using the Tenengrad algorithm.
4. `get_best_image(folder_path, sharpness_method)`: Determines the best image with the highest sharpness using the specified sharpness sorting method.
5. `display_image(image_path)`: Loads and displays the image in its original size.


# 7. Corner Detection

The corner detection feature allows you to identify and locate corners in images. It is commonly used in various computer vision tasks, such as image matching, tracking, and feature extraction.

## Available Corner Detection Methods

1. **Harris Corner Detection**: Applies the Harris corner detection algorithm to identify corners based on local intensity variations.
2. **Shi-Tomasi Corner Detection**: Utilizes the Shi-Tomasi algorithm to detect corners based on the minimum eigenvalue of the gradient matrix.
3. **FAST (Features from Accelerated Segment Test)**: Performs corner detection using the FAST algorithm, which focuses on finding prominent corners quickly.

## Usage

1. Prepare a folder containing the images for corner detection.
2. Set the folder path in the code.
3. Choose the desired corner detection method by specifying it in the code through the `corner_method` parameter.
4. Run the code to identify and display the image with the most detected corners.

## How Code Works

1. `get_best_image(folder_path, corner_method)`: Iterates over the images in the specified folder and applies the chosen corner detection method to find the image with the most corners.
2. `display_image(image_path)`: Loads and displays the best image in its original size, along with printing its name.


