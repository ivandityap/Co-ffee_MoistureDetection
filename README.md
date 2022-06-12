<p align="center">
  <img width="500" alt="logo" src="https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Images/logo2.svg"/>
</p>

[![](https://img.shields.io/badge/ID%20Team-C22_PC377-blue)](https://github.com/xrizer/Co-ffee)
[![PyPI version](https://badge.fury.io/py/autokeras.svg)](https://badge.fury.io/py/autokeras)
![Python](https://img.shields.io/badge/python-v3.9.0+-success.svg)
![Tensorflow](https://img.shields.io/badge/tensorflow-v2.8.0+-success.svg)


**Coffee Beans Moisture Detection with Fusioned Triple Deep Convolutional Neural Network**
## Graphical Abstract
![graph_abs](images/Graphic%20abstract-Page-5.png)
<p align="center">
    <b>Fig 1</b> Triple deep convolutional neural network model for moisture level detection
</p>

## Dataset
**The dataset for this work is manually collected**

The dataset used for this work is images of coffee beans with different moisture. There is 5 different classification:

![dataset](images/dataset.jpeg)

There are total 416 images splitted into train_data, validation_data, and test_data.
You can find the dataset here: **<a target=blank_ href="https://drive.google.com/drive/folders/1WaI9rQo7gBEZzdL7b40X_ciEuAy9DC-R?usp=sharing">Google Drive Prepared Dataset<a/>**

`Dataset Size : 411MB`


## Models
Transfer learning and model fusion is used in this work. There are 3 fusioned model :
- InceptionV3
- VGG16
- DenseNet121

**For an immediate simulation without the hassle of going over the previous instructions, refer to this link. : <a href="https://drive.google.com/file/d/11ycNNk1YWZGSVtpbrCJ3zwIBZgwxd7ai/view?usp=sharing">Pre-Trained Weights</a>**

`PRE-TRAINED WEIGHTS FILESIZE: (344 MB)`

## How To Use
1. Open the `TDCNN_1.ipynb` file in `Co-ffee_MoistureDetection/Model Trainer/`
2. Import all the required libraries.
3. Build the model with transfer learning of `InceptionV3`, `VGG16`, and `DenseNet121`. 
4. Fuse the previous three transfer learning model into one model and make sure when all this three is fused, they have the same input layer.
5. Download the dataset from the [link](https://drive.google.com/drive/folders/1WaI9rQo7gBEZzdL7b40X_ciEuAy9DC-R?usp=sharing) and load it into `ImageDataGenerator` with `.flow_from_directory`
6. Start the training.
7. After all T-DCNN models are built, you may now run the `testing.py` from the main `Co-ffee_MoistureDetection/` folder.
8. Follow through the given instructions and make sure to use the test sample from the provided `/test/` folder
## Results
###### Accuracy and loss graph after 25 epochs.
![Co-ffee logo](https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Images/res1.png)
![Co-ffee logo](https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Images/Screenshot%202022-06-12%20135755.png)
