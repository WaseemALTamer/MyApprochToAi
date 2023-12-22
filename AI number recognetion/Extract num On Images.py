from sklearn.datasets import fetch_openml

# Load the MNIST dataset with 'parser' set to 'auto'
mnist = fetch_openml('mnist_784', parser='auto')

# Extract the labels
y = mnist.target.astype('int')

# Create and write the labels to a text file
output_file = 'mnist_image_labels.txt'

with open(output_file, 'w') as file:
    for label in y:
        file.write(f'{label}\n')

print(f'Image labels saved to {output_file}')