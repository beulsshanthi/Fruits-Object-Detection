import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os

st.title("🍎🍌🍊 Fruit Detection App")

# Load your trained model (repo-la irukku)
model = YOLO("best.pt")  

# Confidence slider
conf_threshold = st.slider("Confidence Threshold", 0.1, 1.0, 0.5, 0.05)

# File uploader for user uploads
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
button=st.button("Detect")

if button:
    if uploaded_file is not None:
        # Load uploaded image
        img = Image.open(uploaded_file).convert('RGB')
        
        # Run detection
        results = model(img, conf=conf_threshold)
        
        # Display image with detections
        st.image(results[0].plot(), caption="Detected Fruits", use_container_width=True)
        
        # Display detected info
        detected_info = []
        for r in results:
            for box, cls, conf in zip(r.boxes.xyxy, r.boxes.cls, r.boxes.conf):
                detected_info.append(f"{model.names[int(cls)]}: {conf:.2f}")
        
        if detected_info:
            st.subheader("Detected Fruits:")
            st.write(detected_info)
        else:
            st.write("No fruits detected. Try lowering the confidence threshold.")