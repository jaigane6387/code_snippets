  ## Demo
 
  [![](https://github.com/jaigane6387/images_classifier/blob/master/demo.png)]

## Overview
when you came across a situation which you want to handle the missing values using KNNImputer,The first thing we need to take care of ,setting a proper K Value. so this is a simple code snippet which helps you to find the best k value . It internally checks the best K value range of [0,23] by fitting the RandomForestClassifier with 10 Folds cross validation.

## Environment Setup
The Code is written in Python 3.6.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/).
you should have scikit-learn and numpy libraries installed in it.

## How to use in your code
 
<ul>
 <li>simply clone this repository </li>
 <li>setup this file in your working Directory</li>
 <li> type the line as shown below in your code</li>
 <li><h5><b> from imputer import knn_impute</b></h5></li>
</ul>
 
