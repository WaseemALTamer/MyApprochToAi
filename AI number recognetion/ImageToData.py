from PIL import Image
import numpy as np


with open('mnist_image_labels.txt', 'r') as file:
    lines = file.readlines()

def image(ImageNum):
    global lines
    PixleArray = []
    image = Image.open(f'mnist_images/mnist_image_{ImageNum}.jpg')
    image_array = np.array(image)
    for i in range(0,len(image_array)):
        for j in range(0,len(image_array[i])):
            PixleArray.append(image_array[i][j])
    for i in range (0,len(PixleArray)):
        PixleArray[i] = PixleArray[i] * 1/255
    return (PixleArray,lines[ImageNum])