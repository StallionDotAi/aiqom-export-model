#from cProfile import label
import tensorflow.keras
import numpy as np
import cv2

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('mymodel.h5')


data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
cam = cv2.VideoCapture(0)

# text = "here we add the text of the label"

while True:
    # _,img = cv2.imread('right.jpg')
    _,img = cam.read()
    img = cv2.resize(img,(224, 224))

    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    labels = prediction[0]
    index = 0
    max = labels[0]

    for i in range(len(labels)):
        if labels[i] > max:
            max = labels[i]
            index = i
    print(index)

    
 # img = cv2.resize(img,(500, 500))
        # cv2.putText(img,text,(10,30),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,0),1)
    cv2.imshow('img',img)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
