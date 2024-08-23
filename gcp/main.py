from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np

potato_model = None
tomato_model = None

potato_class_names = ["Early Blight", "Late Blight", "Healthy"]
tomato_class_names = ["Bacterial Spot",
 "Early Blight",
 "Late Blight",
 "Leaf Mold",
 "Septoril Leaf Spot",
 "Target Spot",
 "YellowLeaf Curl Virus",
 "Mosaic Virus",
 "Healthy"]

BUCKET_NAME = "mabel_project_bucket2"

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

def predict_potato(request):
    global potato_model
    if potato_model is None:
        download_blob(
            BUCKET_NAME,
            "models/potatoes_model1.h5",
            "/tmp/potatoes_model1.h5",
        )
        model = tf.keras.models.load_model("/tmp/potatoes_model1.h5")

    image = request.files["file"]

    image = np.array(
        Image.open(image).convert("RGB").resize((256, 256)) # image resizing
    )

    image = image/255 # normalize the image in 0 to 1 range

    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)

    print("Predictions:",predictions)

    predicted_class = potato_class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return {"class": predicted_class, "confidence": confidence}

def predict_tomato(request):
    global tomato_model
    if tomato_model is None:
        download_blob(
            BUCKET_NAME,
            "models/tomatoes_model1.h5",
            "/tmp/tomatoes_model1.h5",
        )
        model = tf.keras.models.load_model("/tmp/tomatoes_model1.h5")

    image = request.files["file"]

    image = np.array(
        Image.open(image).convert("RGB").resize((256, 256)) # image resizing
    )

    image = image/255 # normalize the image in 0 to 1 range

    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)

    print("Predictions:",predictions)

    predicted_class = tomato_class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return {"class": predicted_class, "confidence": confidence}