import tensorflow as tf
import numpy as np
from keras.models import load_model

# Load the Keras model
model = load_model('models\model.h5')

# Build the SavedModel
export_path = 'modelserver'
tf.saved_model.save(model, export_path)