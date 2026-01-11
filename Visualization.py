from ultralytics import YOLO
import matplotlib.pyplot as plt
import glob
import cv2

model=YOLO("best.pt")

image_paths=glob.glob(r"F:\Fruits Object Detection\Fruits images\*.jpg")

plt.figure(figsize=(20,10))

for i,image in enumerate(image_paths[:4]):
    img=cv2.imread(image)
    results=model(img)
    out=results[0].plot()
    out_rgb=cv2.cvtColor(out,cv2.COLOR_BGR2RGB)
    plt.subplot(2,2,i+1)
    plt.imshow(out_rgb)
    plt.axis("off")

plt.tight_layout()

plt.show()
