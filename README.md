# 🐱🐶 Cat vs Dog AI

A deep learning image classification project that identifies whether an uploaded image contains a **Cat** or a **Dog**.

The project includes a trained image classification model and a user-friendly interface for making predictions from uploaded images.

## 🚀 Features

* 🐱 Cat vs Dog image classification
* 🧠 Deep learning-based image recognition
* 🖼️ Upload an image and receive a prediction
* 📊 Displays the model's prediction
* 🌐 Streamlit-based user interface
* ⚡ Can run locally on a PC

## 🛠️ Technologies Used

* Python
* PyTorch
* Streamlit
* Pillow
* NumPy
* Matplotlib

## 📂 Project Structure

```text
cat-dog-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── ...
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Adwaithdk/cat-dog-ai.git
```

### 2. Open the project folder

```bash
cd cat-dog-ai
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

### 5. Install the required libraries

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 How It Works

The application follows a simple image-classification pipeline:

```text
Input Image
     ↓
Image Preprocessing
     ↓
Deep Learning Model
     ↓
Prediction
     ↓
Cat / Dog
```

The uploaded image is processed into the format expected by the trained model. The model then predicts whether the image belongs to the Cat or Dog class.

## 📊 Model Performance

**Test Accuracy:** Add your accuracy here

**Model Architecture:** Add your model architecture here

**Training Dataset:** Add your dataset information here

## 🖥️ Application

The project provides a Streamlit interface where users can upload an image and receive a Cat/Dog prediction.

*Add a screenshot of your application here.*

## 🔮 Future Improvements

* Improve model accuracy
* Add confidence scores
* Support additional animal classes
* Improve the user interface
* Deploy the application online
* Add data augmentation and advanced model architectures

## 👨‍💻 Author

**Adwaith Dinesh K**

Cyber Security Student

GitHub: [@Adwaithdk](https://github.com/Adwaithdk)
