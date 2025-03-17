
from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import os
import gdown
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Google Drive File ID (Extracted from the link)
file_id = "1NkChDFdZX40LiZl9_7x2tMJegqTmrCvI"  # Corrected File ID

# Model file path
MODEL_PATH = "eurosat_cnn_model.h5"

# Check if model exists, if not, download it
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", MODEL_PATH, quiet=False)

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)
print("Model Loaded Successfully!")

# Define class labels
class_labels = [
    "AnnualCrop", "Forest", "Highway", "Industrial", "Pasture",
    "PermanentCrop", "Residential", "River", "SeaLake", "HerbaceousVegetation"
]

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def predict_image(img_path):
    """Function to predict image class"""
    img = image.load_img(img_path, target_size=(128, 128))  # Resize image
    img_array = image.img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    class_label = class_labels[class_index]

    return class_label

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            result = predict_image(file_path)

            return render_template("index.html", prediction=result, img_path=file_path)

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
