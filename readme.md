---
title: Fruit Object Detection
emoji: 🍎
colorFrom: green
colorTo: blue
sdk: docker
app_file: app.py
pinned: false
---

# 🍎🍌🍊 Fruit Object Detection using YOLOv8

This project implements **fruit detection (Apple, Banana, Orange)** using **Ultralytics YOLOv8**.  
The dataset contains images of three classes and was trained, validated, and tested using custom augmentation.  
The final model is deployed with a **Streamlit App** and hosted on **AWS/GCP** for real-time inference.

---

## 📌 **Project Overview**

This project identifies three fruit classes:

- **Apple (class 0)**
- **Banana (class 1)**
- **Orange (class 2)**  

## 📁 Project Structure

project/
├── yolo_data/
│   ├── images/
│   │   ├── train/
│   │   ├── valid/
│   │   ├── test/
│   ├── labels/
│   │   ├── train/
│   │   ├── valid/
│   │   ├── test/
├── best.pt
├── fruit_streamlit.py
└── data.yaml


---

## 🚀 Model Summary

- Model: **YOLOv8s**
- Epochs: **80**
- Device: **Google Colab GPU**
- Early stopping enabled
- Augmentation applied:
  - Horizontal Flip  
  - Brightness/Contrast  
  - Rotation  
  - Color Jitter  
  - Motion/Motion Blur  
  - Random Shadows  
- **Number of classes = 3**  
  - apple  
  - banana  
  - orange  

---

## 📊 Final Evaluation Metrics

Your final training metrics (real values):

### **Per-Class Scores**
| Class   | Precision | Recall | F1-Score |
|---------|-----------|--------|----------|
| Apple   | **0.99447** | **0.99999** | **0.99723** |
| Banana  | **0.99847** | **0.96875** | **0.98339** |
| Orange  | **0.94999** | **0.96444** | **0.95497** |

---

### **Mean Scores**
| Metric     | Value |
|------------|--------|
| **mAP50**      | **0.99266** |
| **mAP50-95**   | **0.85848** |

---

## 🔲 Confusion Matrix

Your final confusion matrix:
[[64, 0, 0, 5],
[0, 63,  0, 4],
[0, 0,  50, 5],
[0, 1, 0,  0]]

---

# Author


- Shanthi Beula Palraj
