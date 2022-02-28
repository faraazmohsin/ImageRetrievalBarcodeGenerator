# ImageRetrievalBarcodeGenerator

<p align="center">
  Development, design methodology, testing, and complexity analysis of a python-based, content retrieval application for the retrieval of images from a set of generated barcodes.
</p>

<p align="center">
  This project is a greater application of data structures, simulating a real-world problem to be solved with the knowledge of data organization, complex algorithms, and binary logic. The end-goal was accomplished with the implementation of two algorithms, one for barcode generation, the other for image retrieval. Barcode generation involved the conversion of provided images into an abstract data type, an array in this case which was broken down further into projections used to calculate the threshold. The threshold was then used in the calculation of hamming distance between multiple data sets, the hamming distance being a metric for the barcode to image accuracy. The data set of the lowest coefficient would finally be selected, thus outputting the correct image.
</p>

<p align="center" width="100%">
  <img src="https://github.com/faraazmohsin/ImageRetrievalBarcodeGenerator/blob/main/images/projectprojection.PNG">
</p>

## Measurements and Analysis

<p align="center">
  In terms of time complexity, calculating the number of operations in the entire code was required. Specifically, an algorithm is usually said to have a constant time when it is not dependent on the input data (n). This is because the input data is not dependent, and the size of the data does not usually matter, the running time will be equal each time too. In addition, because we do not have to specifically consider the input size, an algorithm with constant time is strong and efficient.
 </p>
