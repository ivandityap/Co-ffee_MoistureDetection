print('Loading ...')

import os
import logging
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

print('Packages loaded')
tf.get_logger().setLevel(logging.ERROR)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


def load_models():
    model = load_model("Model\TDCNN.h5")
    print('model loading complete')
    return model

labels = {
    '13 %': 0,
    '13.2 %': 1,
    '14 %': 2,
    '15 %': 3,
    '> 15 %': 4
}
def get_label(index,labels=labels):
   for class_string, class_index in labels.items():
      if class_index == index:
         return class_string

def show_predict(model, preprocessed_image):
    classes = model.predict(preprocessed_image)
    predicted_index = np.argmax(classes[0])
    confidence = max(100 * classes[0])
    return predicted_index, confidence

def report(result, peluang):
    hasil = f'{get_label(result)} ({peluang:.2f} %)'
    return hasil
    
def main(img_path, model):
    img=load_img(img_path, target_size=(224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    result, peluang = show_predict(model, x)

    return result, peluang

if __name__ == "__main__":
    path = 'Test/'
    model = load_models()

    while True:
        while True:
            try:
                img_path = path + input('input image :')
                result, peluang = main(img_path, model)
            except IOError:
                print(
                    "The image was not found or is invalid. Please try again, or press CTRL+C to exit the program..."
                )
            else:
                break
        
        print(img_path)
        hasil = report(result, peluang)
        print(hasil)
        print("\nClose the image window to continue. . .")
        img = load_img(img_path, target_size=(224, 224))
        plt.imshow(img)
        plt.show()




