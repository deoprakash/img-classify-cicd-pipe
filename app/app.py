from flask import Flask, request, render_template, jsonify
from utils import preprocess_image
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model("app/model.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        image = request.files['image']
        img_arr = preprocess_image(image)
        pred = model.predict(np.expand_dims(img_arr, axis=0))[0][0]
        label = "airplane" if pred < 0.5 else "automobile"
        return render_template('index.html', prediction=label)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
