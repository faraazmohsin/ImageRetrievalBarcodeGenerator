import csv

import numpy
import numpy as np
from PIL import Image
from numpy import asarray
import os

# link to image files
for subdir, dirs, files in os.walk(r'C:\Users\Faraaz\Documents\GitHub\ImageRetrievalBarcodeGenerator\MNIST_DS'):
    for filename in files:
        filepath = subdir + os.sep + filename

        # print image files
        if filepath.endswith(".jpg"):
            print(filepath)

image = Image.open(r'C:\Users\Faraaz\Documents\GitHub\ImageRetrievalBarcodeGenerator\MNIST_DS\0\img_10007.jpg')

numpy_data = asarray(image)

print(numpy_data)
print('\n')

# Projections
p = numpy.array(image)

# Array data 1
array1 = []

# Threshold data 1
th1 = []

# numpy.sum to project angle 0
array1 = np.sum(p, 1)

print("Array Projection 1 = ")
print(array1)
print('\n')

# Calculate the threshold value by dividing sum of array data by number of index in the array
th_p1 = sum(array1) / len(array1)

print("Threshold value of P1 = ")
print(th_p1)
print('\n')

# Barcode generator algorithm for barcode 1
for x in range(len(array1)):
    if th_p1 >= array1[x]:
        th1 = [*th1, 0]
    else:
        th1 = [*th1, 1]

print("barcode 1 = ")
print(th1)
print('\n')

# Array data 2
array2 = []

# Threshold data 2
th2 = []

# numpy.sum to project angle 0
array0 = np.sum(p, 1)

# numpy.sum to project angle 45
array45 = np.sum(p, 0)

joinedarray1 = array0 + array45
print(joinedarray1)
print('\n')

# Calculate threshold value by dividing sum of array data by number of index in the array
th2_p2 = sum(joinedarray1) / len(joinedarray1)

# Barcode generator algorithm for barcode 2
for y in range(len(array2)):
    if th2_p2 >= array2[y]:
        th2 = [*th2, 0]
    else:
        th2 = [*th2, 1]

print("Array Projection 2 = ")
print(array0)
print('\n')
print(array45)
print('\n')

print("Threshold value of P2 = ")
print(th2_p2)
print('\n')

print("barcode 2 = ")
print(th2)
print('\n')

# Array data 3
array3 = []

# Threshold data 3
th3 = []

# numpy.sum to project angle 90
array3 = np.sum(p, 0)

print("Array Projection 3 = ")
print(array3)
print("\n")

# Calculate threshold value by dividing sum of array data by number of index in the array
th3_p3 = sum(array3) / len(array3)

print("Threshold value of P3 = ")
print(th3_p3)
print("\n")

# Barcode generator algorithm for barcode 3
for z in range(len(array3)):
    if th3_p3 >= array3[z]:
        th3 = [*th3, 1]
    else:
        th3 = [*th3, 0]

print("barcode 3 = ")
print(th3)
print("\n")

# Array data 4
array4 = []

# Threshold data 4
th4 = []

# numpy.sum to project angle 0
array0 = np.sum(p, 1)

# numpy.sum to project angle 45
array45 = np.sum(p, 0)

joinedarray2 = ((array0 + array45) / 2)
array4 = joinedarray2 + array45

# Calculate threshold value by dividing sum of array data by number of index in the array
th4_p4 = sum(array4) / len(array4)

# Barcode generator algorithm for barcode 4
for w in range(len(array4)):
    if th4_p4 >= array4[w]:
        th4 = [*th4, 1]
    else:
        th4 = [*th4, 0]

print("Array Projection 4 = ")
print(array4)
print("\n")

print("Threshold value of P4 = ")
print(th4_p4)
print("\n")

print("barcode 4 = ")
print(th4)
print("\n")


# Search

class data:

    # Calculate hamming distance
    def h(self, u, y):
        hamming = 0

        for c in range(len(u)):

            value1, value2 = int(u[c]), int(y[c])
            if value1 != value2:
                hamming += 1
            else:
                return

    # Define constructor for barcode
    def __init__(self, start, barcode):
        self.fileLocationHam
        self.flocationHam
        self.hm = []
        self.start = start
        self.barcode = barcode

    # Calculate total accuracy
    def acc(self, sort):
        fname = str(sort[0][1])
        compute = int(fname[24])
        counter = 0

        # Calculate accuracy from hamming distance
        for c in range(10):
            aBar = str(sort[c][1])
            new = int(aBar[24])
            if compute == aBar:
                counter += 1

            return (counter - 1) / 9

    if __name__ == "__data__":

        fpData = []
        bdData = []

        # Load all images in dataset
        for subdir, dirs, files in os.walk(r'C:\Users\Faraaz\Documents\GitHub\ImageRetrievalBarcodeGenerator\MNIST_DS'):
            for filename in files:
                filepath = subdir + os.sep + filename

                if filepath.endswith(".jpg"):
                    print(filepath)

        # Set barcode to image
        for f in range(len(fpData)):
            image = Image.open(fpData[f])
            imageArray = np.asarray(image)
            barcode = numpy_data

        # List barcode per from zipfile
        barcode = list(zip(fpData, bdData))

        # Write and print barcodes in file
        with open('barcode.txt', 'w') as result:
            w = csv.writer(result, dialect='Notepad')
