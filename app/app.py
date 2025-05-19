from flask import Flask, request, render_template, jsonify
from utils import preprocess_image
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model("model.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        image = request.files['image']
        img_arr = preprocess_image(image)
        result = model.predict(np.array([img_arr]))[0]
        prediction = str(np.argmax(result))
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
