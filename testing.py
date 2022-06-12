import os
import logging

import tensorflow as tf
# import cv2
import matplotlib.pyplot as plt
import numpy as np

from efficientnet.keras import preprocess_input

import keras
from keras.models import load_model
from keras.utils import load_img, img_to_array
# from keras import applications

tf.get_logger().setLevel(logging.ERROR)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def load_models():
    model = load_model("weights/TDCNN_1.h5")
    print('model loading complete')
    return model

def labels(n_stage):
    label= {
        '<13' : 0,
        '<13.2' : 1,
        '<14' : 2,
        '<15' : 3,
        '15>' : 4
    }
    return label

def get_label(index,n_stage):
   for class_string, class_index in labels(n_stage).items():
      if class_index == index:
         return class_string

def show_predict(model, preprocessed_image):
    classes = model.predict(preprocessed_image)
    predicted_index = np.argmax(classes[0])
    confidence = max(100 * classes[0])
    return predicted_index, confidence
    return show+predict

def report(result, peluang, count):
    for i in range(count):
        print()
        print(f'Result : {get_label(result,i)}')
        print(f'Confidence level : {peluang:.2f} %')
    
def main(img_path, model):
    img=load_img(img_path,target_size=(224,224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    index, confidence = 0, 0
    index, confidence = show_predict(model,x)
    count = 1
    return index, confidence, count

if __name__ == "__main__":
    path = 'test1/'
    model = load_models()

    while True:
        while True:
            try:
                img_path = path + input('Please enter a file from your test folder with the coffee leaf images ex: (2.jpg):')
                result, peluang, count = main(img_path, model)
            except IOError:
                print(
                    "The image was not found or is invalid. Please try again, or press CTRL+C to exit the program..."
                )
            else:
                break
        
        print(img_path)
        report(result, peluang, count)
        print("\nClose the image window to continue. . .")
        img=load_img(img_path,target_size=(224,224))
        plt.imshow(img)
        plt.show()







