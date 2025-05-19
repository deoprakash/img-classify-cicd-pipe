from PIL import Image
import numpy as np

def preprocess_image(file):
    img = Image.open(file).resize((32, 32), resample=Image.Resampling.LANCZOS)
    img_arr = np.array(img)/ 255.0
    return img_arr