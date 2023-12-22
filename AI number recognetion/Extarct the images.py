from sklearn.datasets import fetch_openml
from PIL import Image
import os

# Load the MNIST dataset with 'parser' set to 'auto'
mnist = fetch_openml('mnist_784', parser='auto')

# Extract the features (pixel values) and labels
X, y = mnist.data, mnist.target

# Convert features to integers and reshape to image dimensions
X = X.astype('int').values.reshape(-1, 28, 28)

# Directory where you want to save the JPG images
output_directory = 'mnist_images'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Save each image as a JPG file after converting to 'L' mode
for i, image_data in enumerate(X):
    image = Image.fromarray(image_data).convert('L')
    image_path = os.path.join(output_directory, f'mnist_image_{i}.jpg')
    image.save(image_path)

print(f'{len(X)} MNIST images saved as JPG files in {output_directory}')