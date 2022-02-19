import numpy
import numpy as np
from PIL import Image
from numpy import asarray
import os

for subdir, dirs, files in os.walk(r'C:\Users\Faraaz\Documents\GitHub\ImageRetrievalBarcodeGenerator\MNIST_DS'):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".jpg"):
            print(filepath)


image = Image.open(r'C:\Users\Faraaz\Documents\GitHub\ImageRetrievalBarcodeGenerator\MNIST_DS\0\img_10007.jpg')

numpy_data = asarray(image)

print(numpy_data)
print('\n')

p = numpy.array(image)
array1 = []
th1 = []
array1 = np.sum(p, 1)

print("Array Projection 1 = ")
print(array1)
print('\n')

th_p1 = sum(array1) / len(array1)

print("Threshold value of P1 = ")
print(th_p1)
print('\n')

for x in range(len(array1)):
    if th_p1 >= array1[x]:
        th1 = [*th1, 0]
    else:
        th1 = [*th1, 1]

print("barcode 1 = ")
print(th1)
print('\n')

