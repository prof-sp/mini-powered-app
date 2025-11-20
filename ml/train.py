import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image_dataset_from_directory
import os

DATA_DIR = "data"  # structure: data/train/<class>/*.jpg and data/val/<class>/*.jpg
BATCH_SIZE = 32
IMG_SIZE = (224,224)
EPOCHS = 10
NUM_CLASSES = 3
SAVED_MODEL_DIR = "saved_models/latest_model"

def prepare_datasets():
    train_ds = image_dataset_from_directory(os.path.join(DATA_DIR,"train"), image_size=IMG_SIZE, batch_size=BATCH_SIZE)
    val_ds = image_dataset_from_directory(os.path.join(DATA_DIR,"val"), image_size=IMG_SIZE, batch_size=BATCH_SIZE)
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.prefetch(AUTOTUNE)
    val_ds = val_ds.prefetch(AUTOTUNE)
    return train_ds, val_ds

def build_model():
    base = EfficientNetB0(include_top=False, input_shape=IMG_SIZE + (3,), weights='imagenet')
    base.trainable = False
    inputs = layers.Input(shape=IMG_SIZE + (3,))
    x = base(inputs, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(NUM_CLASSES, activation='softmax')(x)
    model = models.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def main():
    train_ds, val_ds = prepare_datasets()
    model = build_model()
    model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS)
    os.makedirs(SAVED_MODEL_DIR, exist_ok=True)
    model.save(SAVED_MODEL_DIR)

if __name__ == "__main__":
    main()
