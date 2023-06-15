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

