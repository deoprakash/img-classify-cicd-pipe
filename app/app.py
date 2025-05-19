from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from app.utils import preprocess_image
import numpy as np

app = Flask(__name__)
model = load_model("app/model.h5")

@app.route('/predict', methods = ['POST'])
def predict():
    if 'image' not  in request.files:
        return jsonify({"error": "No image uploaded"}), 400


    image = request.files["image"]
    img_arr = preprocess_image(image)
    pred = model.predict(np.expand_dims(img_arr, axis=1))[0][0]
    label = "airplane" if pred < 0.5 else "automobile"
    return jsonify({"prediction": label})

