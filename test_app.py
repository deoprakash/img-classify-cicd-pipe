import requests

def test_prediction():
    url = "http://localhost:5000/predict"
    files = {'image': open('data/sample.jpg', 'rb')}
    response = requests.post(url, files=files)
    
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    assert response.status_code == 200

test_prediction()
