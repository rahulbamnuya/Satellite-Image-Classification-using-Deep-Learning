# Satellite Image Classification using Deep Learning

This project is a **Satellite Image Classification** system that uses a **Convolutional Neural Network (CNN)** to classify satellite images into different categories. The model has been trained on the **EuroSAT dataset** and can identify 10 different land cover types.

## 🚀 Features
- Classifies satellite images into **10 different classes**
- Uses a **trained CNN model** for accurate predictions
- Web-based interface using **Flask** for easy image uploads and classification
- Model is stored on **Google Drive** and downloaded automatically when needed
- Supports **real-time image predictions**

## 🏷️ Classes
The model can classify images into the following categories:
- 🌱 **AnnualCrop**
- 🌳 **Forest**
- 🛣️ **Highway**
- 🏭 **Industrial**
- 🐄 **Pasture**
- 🌾 **PermanentCrop**
- 🏡 **Residential**
- 🌊 **River**
- 🌊 **SeaLake**
- 🌿 **HerbaceousVegetation**

---

## 📂 Project Structure
```
Satellite-Image-Classification/
│── static/                 # Stores uploaded images
│── templates/              # HTML templates (index.html)
│── app.py                  # Main Flask application
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

## ⚙️ Installation & Setup
To set up this project on your local machine, follow these steps:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Satellite-Image-Classification-using-Deep-Learning.git
cd Satellite-Image-Classification-using-Deep-Learning
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App
```bash
python app.py
```
This will start the web application, and you can access it in your browser at:
```
http://127.0.0.1:5000/
```

---

## 📥 How to Use
1. Upload a **satellite image** in `.jpg`, `.png`, or `.jpeg` format.
2. Click the **Upload & Predict** button.
3. The model will classify the image into one of the **10 categories**.
4. The predicted class will be displayed on the screen.

---
## Screenshots

# Home Page:

![Screenshot (30)](https://github.com/user-attachments/assets/42de1c34-b4f9-4913-ba6b-1c2a7e3a97ac)


# Uploading an Image:

![Screenshot (30)](https://github.com/user-attachments/assets/ee286872-f183-4113-9808-21f066539fdb)


# Prediction Result:
![Screenshot (29)](https://github.com/user-attachments/assets/595a7bf0-b321-4ed9-a8df-6066c6afad85)

## 📦 Model Details
- The model is trained using a **CNN (Convolutional Neural Network)** on the **EuroSAT dataset**.
- It is saved as a **TensorFlow Keras model** in `.h5` format.
- The model file (`eurosat_cnn_model.h5`) is **too large for GitHub**, so it is stored on **Google Drive** and downloaded automatically.

### 🔗 Google Drive Model Link
[Download Model](https://drive.google.com/file/d/1NkChDFdZX40LiZl9_7x2tMJegqTmrCvI/view?usp=sharing)

### Model Architecture
- **Input Layer**: 128x128 RGB images
- **Convolutional Layers**: Extract features from images
- **Fully Connected Layers**: Classify the image into one of 10 categories
- **Activation Functions**: ReLU & Softmax
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy

---

## 💡 Troubleshooting
**Issue: `ModuleNotFoundError: No module named 'gdown'`**  
➡️ Run: `pip install gdown`

**Issue: Model not downloading from Google Drive**  
➡️ Check your internet connection and retry running `app.py`

---

## 📜 License
This project is open-source and available under the **MIT License**.

## 🤝 Contributing
Feel free to **fork** this repository, improve it, and create a **pull request**!

## 📧 Contact
For any queries or suggestions, reach out to:
📩 **rahulbamniya93184@gmail.com**

