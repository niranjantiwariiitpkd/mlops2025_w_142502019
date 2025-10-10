# Members:
  1. **Uma Mahesh** : 142502018
  2. **Niranjan Tiwari** : 142502019

-------------------------------------
# Forest Fire & Smoke Detection

##  Overview
Wildfires cause severe environmental and economic damage, and **early smoke detection** is crucial for timely intervention.  
This project implements a **deep learning‑based image classification system** to detect **Fire**, **Smoke**, and **Non‑Fire** scenes from images, enabling faster and more reliable wildfire alerts.

The system uses a **ResNet‑18** model trained on the [PyroNear SDIS dataset](https://huggingface.co/datasets/pyronear/pyro-sdis), fine‑tuned with data augmentation and class‑balanced loss to handle diverse environmental conditions.

---

##  Objectives
- Develop an automated deep learning‑based system to detect and classify **Fire**, **Smoke**, and **Non‑Fire** images.
- Handle diverse environmental conditions and smoke appearances.
- Minimize false positives and false negatives for reliable early alerts.
- Provide an **interactive Gradio web app** for easy testing.

---

##  Dataset
- **Name:** PyroNear SDIS Dataset  
- **Size:** ~33,600 images of wildfire smoke  
- **Source:** Captured from Pyronear’s camera network in collaboration with SDIS (Fire and Rescue Services) in France  
- **Annotations:** YOLO format (class_id, x_center, y_center, width, height)  
- **License:** Apache‑2.0  
- **Purpose:** Suitable for training deep learning models for smoke detection and localization under diverse environmental conditions  
- **Link:** [PyroNear SDIS Dataset](https://huggingface.co/datasets/pyronear/pyro-sdis)

---

##  Tech Stack
- **Python 3.x**
- **PyTorch** — Model training & inference
- **Torchvision** — Pretrained models & transforms
- **Gradio** — Web interface
- **Matplotlib / NumPy** — Visualization & data handling
- **Pillow** — Image processing
- **scikit‑learn** — Metrics & class weights

---
 Project Structure
```
Forest_Fire_Smoke_Detection/
├── code/
│   ├── 142502019_ml_ops_project_version1.ipynb       # Gradio web app
├── models/
│   └── fire_smoke_model.pth        # Saved trained model
├── docs/
│   └── project_presentation.pptx
├── requirements.txt
├── README.md
```

---

##  Installation
1. **Clone the repository**

git clone https://githubcomyourusernameForest_Fire_Smoke_Detection.git

cd Forest_Fire_Smoke_Detection

python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

pip install -r requirements.txt

python code/142502019_ml_ops_project_version1.ipynb


Example output:

Prediction: Fire (98.39%)
Probalilities:

    Fire: 98.39%
    Smoke: 1.20%
    Non‑Fire: 0.41%


Future Improvements
    Deploy the Gradio app online.

    Add real‑time video stream detection.

    Use a larger pretrained model (e.g., EfficientNet).
    

    Collect more diverse training data.
