# ImageRetrievalBarcodeGenerator

<p align="center">
  Development, design methodology, testing, and complexity analysis of a python-based, content retrieval application for the retrieval of images from a set of generated barcodes.
</p>

<p align="center">
  This project is a greater application of data structures, simulating a real-world problem to be solved with the knowledge of data organization, complex algorithms, and binary logic. The end-goal was accomplished with the implementation of two algorithms, one for barcode generation, the other for image retrieval. Barcode generation involved the conversion of provided images into an abstract data type, an array in this case which was broken down further into projections used to calculate the threshold. The threshold was then used in the calculation of hamming distance between multiple data sets, the hamming distance being a metric for the barcode to image accuracy. The data set of the lowest coefficient would finally be selected, thus outputting the correct image.
</p>

<p align="center">
![alt text](https://github.com/faraazmohsin/ImageRetrievalBarcodeGenerator/blob/main/images/projectprojection.PNG)
</p>
