import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

# Page settings
st.set_page_config(
    page_title="Cat vs Dog AI",
    page_icon="🐱",
)

# Load model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 2)

model.load_state_dict(
    torch.load(
        "cat_dog_model.pth",
        map_location=device
    )
)

model = model.to(device)
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

classes = ["Cat", "Dog"]

# Website
st.title("🐱 Cat vs Dog AI 🐶")

st.write(
    "Upload an image and let my AI model predict whether it is a cat or a dog."
)

uploaded_file = st.file_uploader(
    "Upload a cat or dog image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Prepare image
    image_tensor = transform(image)
    image_tensor = image_tensor.unsqueeze(0)
    image_tensor = image_tensor.to(device)

    # Prediction
    with torch.no_grad():

        output = model(image_tensor)

        probabilities = torch.softmax(output, dim=1)

        predicted_class = torch.argmax(
            probabilities,
            dim=1
        ).item()

        confidence = probabilities[0][predicted_class].item()

    prediction = classes[predicted_class]

    # Display result
    st.subheader("Prediction")

    if prediction == "Cat":
        st.success(
            f"🐱 Cat — {confidence * 100:.2f}% confidence"
        )
    else:
        st.success(
            f"🐶 Dog — {confidence * 100:.2f}% confidence"
        )