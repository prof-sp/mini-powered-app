import tensorflow as tf
import os

SAVED_MODEL_DIR = "saved_models/latest_model"
TFLITE_PATH = "saved_models/model.tflite"

def convert():
    model = tf.keras.models.load_model(SAVED_MODEL_DIR)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()
    with open(TFLITE_PATH, "wb") as f:
        f.write(tflite_model)
    print("Saved tflite to", TFLITE_PATH)

if __name__ == "__main__":
    convert()
