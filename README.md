![Co-ffee logo](https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Images/logo2.svg)
## Coffee Beans Moisture Detection with Fusioned Triple Deep Convolutional Neural Network
# DATASETS
##### The dataset is manually collected by us
The dataset used for this work is images of coffee beans with different moisture. There is 5 different classification:
- <13%
  - <img src= "https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Dataset/Fk0%20(9).jpg" width="250" height="200">
- <13.2%
  - <img src= "https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Dataset/RBT3k1%20(3).jpg" width="250" height="200">
- <14%
  - <img src= "https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Dataset/Fk2%20(3).jpg" width="250" height="200">
- <15%
  - <img src= "https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Dataset/Fk3%20(5).jpg" width="250" height="200">
- 15%>
  - <img src= "https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Dataset/6k4%20(1).jpg" width="250" height="200">

There are total 416 images splitted into train_data, validation_data, and test_data.
# Models
Transfer learning and model fusion is used in this work. There are 3 fusioned model :
- InceptionV3
- VGG16
- DenseNet121
# How To Use
1. Open the `TDCNN_1.ipynb` file in `Co-ffee_MoistureDetection/Model Trainer/`
2. Import all the required libraries.
3. Build the model with transfer learning of `InceptionV3`, `VGG16`, and `DenseNet121`. 
4. Fuse the previous three transfer learning model into one model and make sure when all this three is fused, they have the same input layer.
5. Download the dataset from the link and load it into `ImageDataGenerator` with `.flow_from_directory`
6. Start the training.
7. After all T-DCNN models are built, you may now run the testing.py from the main `Co-ffee_MoistureDetection/` folder.
8. Follow through the given instructions and make sure to use the test sample from the provided `/test/` folder
# Results
###### Accuracy and loss graph after 25 epochs.
![Co-ffee logo](https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Images/res1.png)
![Co-ffee logo](https://github.com/ivandityap/Co-ffee_MoistureDetection/blob/main/Images/Screenshot%202022-06-12%20135755.png)
