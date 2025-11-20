from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

MODEL_PATH = os.getenv("MODEL_PATH", "ml/saved_models/latest_model.h5")
# load once
_model = None

def load_tf_model():
    global _model
    if _model is None:
        _model = load_model(MODEL_PATH)
    return _model

def preprocess_image_bytes(image_bytes, target_size=(224,224)):
    img = Image.open(image_bytes).convert("RGB")
    img = img.resize(target_size)
    arr = np.array(img) / 255.0
    return np.expand_dims(arr, 0)

def predict(image_file):
    model = load_tf_model()
    x = preprocess_image_bytes(image_file)
    preds = model.predict(x)[0]
    # assume classes in order ['Fresh','Spoiled','Contaminated']
    classes = ['Fresh','Spoiled','Contaminated']
    idx = int(np.argmax(preds))
    return {"label": classes[idx], "confidence": float(preds[idx])}
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

MODEL_PATH = os.getenv("MODEL_PATH", "ml/saved_models/latest_model.h5")
# load once
_model = None

def load_tf_model():
    global _model
    if _model is None:
        _model = load_model(MODEL_PATH)
    return _model

def preprocess_image_bytes(image_bytes, target_size=(224,224)):
    img = Image.open(image_bytes).convert("RGB")
    img = img.resize(target_size)
    arr = np.array(img) / 255.0
    return np.expand_dims(arr, 0)

def predict(image_file):
    model = load_tf_model()
    x = preprocess_image_bytes(image_file)
    preds = model.predict(x)[0]
    # assume classes in order ['Fresh','Spoiled','Contaminated']
    classes = ['Fresh','Spoiled','Contaminated']
    idx = int(np.argmax(preds))
    return {"label": classes[idx], "confidence": float(preds[idx])}
