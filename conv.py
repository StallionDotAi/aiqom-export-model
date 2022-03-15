from tensorflow import keras
import os
import sys
import tensorflow as tf
from tensorflow.keras.preprocessing import image

pb_model_dir = sys.argv[1]
if os.path.exists(pb_model_dir):
    print (os.path.basename(pb_model_dir))

##put it as arg in the command
#pb_model_dir = "keras"

h5_model = "mymodel.h5"

# Loading the Tensorflow Saved Model (PB)
model = tf.keras.models.load_model(pb_model_dir)
print(model.summary())

# Saving the Model in H5 Format
tf.keras.models.save_model(model, h5_model)

# Loading the H5 Saved Model
loaded_model_from_h5 = tf.keras.models.load_model(h5_model)
print(loaded_model_from_h5.summary())
