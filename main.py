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


array2 = []
th2 = []
array0 = np.sum(p, 1)
array45 = np.sum(p, 0)

print("Array Projection 2 = ")
print(array0)
print('\n')
print(array45)
print('\n')

joinedarray1 = array0 + array45
print(joinedarray1)
print('\n')

th2_p2 = sum(joinedarray1) / len(joinedarray1)

print("Threshold value of P2 = ")
print(th2_p2)
print('\n')

for y in range(len(array2)):
    if th2_p2 >= array2[y]:
        th2 = [*th2, 0]
    else:
        th2 = [*th2, 1]

print("barcode 2 = ")
print("th2")
print('\n')

array3 = []
th3 = []
array3 = np.sum(p, 0)

print("Array Projection 3 = ")
print(array3)
print("\n")

th3_p3 = sum(array3) / len(array3)

print("Threshold value of P3 = ")
print(th3_p3)
print("\n")

for z in range(len(array3)):
    if th3_p3 >= array3[z]:
        th3 = [*th3, 1]
    else:
        th3 = [*th3, 0]

print("barcode 3 = ")
print(th3)
print("\n")

array4 = []
print("Array Projection 4 = ")
print(array4)
print("\n")

th4 = []

array0 = np.sum(p, 1)
array45 = np.sum(p, 0)

joinedarray2 = ((array0 + array45)/2)
array4 = joinedarray2 + array45

th4_p4 = sum(array4) / len(array4)

print("Threshold value of P4 = ")
print(th4_p4)
print("\n")

for w in range(len(array4)):
    if th4_p4 >= array4[w]:
        th4 = [*th4, 1]
    else:
        th4 = [*th4, 0]

print("barcode 4 = ")
print(th4)
print("\n")