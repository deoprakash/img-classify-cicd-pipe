# test_app.py
import requests

def test_prediction():
    url = "http://localhost:5000/predict"
    with open("data/sample.jpg", "rb") as f:
        files = {"image": f}
        response = requests.post(url, files=files)
        assert response.status_code == 200
        assert "prediction" in response.json()

if __name__ == "__main__":
    test_prediction()
