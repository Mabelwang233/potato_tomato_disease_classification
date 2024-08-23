from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define endpoints for potato and tomato
endpoints = {
    "potato": "http://localhost:8601/v1/models/plant_disease_model/labels/potato:predict",
    "tomato": "http://localhost:8601/v1/models/plant_disease_model/labels/tomato:predict"
}

# Class names for potato and tomato models
class_names = {
    "potato": ["Early Blight", "Late Blight", "Healthy"],
    "tomato": ["Bacterial Spot",
 "Early Blight",
 "Late Blight",
 "Leaf Mold",
 "Septoril Leaf Spot",
 "Target Spot",
 "YellowLeaf Curl Virus",
 "Mosaic Virus",
 "Healthy"]
}

@app.get("/ping")
async def ping():
    return "Hello, alive!"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

async def make_prediction(model_type: str, file: UploadFile):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    json_data = {
        "instances": img_batch.tolist()
    }

    response = requests.post(endpoints[model_type], json=json_data)
    prediction = np.array(response.json()["predictions"][0])
    print(response.json()["predictions"])
    predicted_class = class_names[model_type][np.argmax(prediction)]
    confidence = np.max(prediction)
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

@app.post("/potato_predict")
async def potato_predict(file: UploadFile = File(...)):
    return await make_prediction("potato", file)

@app.post("/tomato_predict")
async def tomato_predict(file: UploadFile = File(...)):
    return await make_prediction("tomato", file)

if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port = 8000)