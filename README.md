# Kidney_Disease_Classification

# What is Kidney tumors?

Kidney tumors (also called renal tumors) are growths in the kidneys that can be benign or cancerous. Most do not cause symptoms and are discovered unexpectedly when you are being diagnosed and teated for another condition.


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?

### Steps:

Clone the repository

```bash
https://github.com/Arunmaheshwari/Kidney_Disease_Classification
```
and then

```bash
cd Kidney_Disease_Classification
```


### Step 01 - Create a virtual environment after opening the repository

```bash
python -m venv venv
```

```bash
venv/Scripts/activate
```

### Step 02 - Install the requirements
```bash
pip install -r requirements.txt
```
























## About Dataset

# Context
CT KIDNEY DATASET: Normal-Cyst-Tumor and Stone

# Content
The dataset was collected from PACS (Picture archiving and communication system) from different hospitals in Dhaka, Bangladesh where patients were already diagnosed with having a kidney tumor, cyst, normal or stone findings. Both the Coronal and Axial cuts were selected from both contrast and non-contrast studies with protocol for the whole abdomen and urogram. The Dicom study was then carefully selected, one diagnosis at a time, and from those we created a batch of Dicom images of the region of interest for each radiological finding. Following that, we excluded each patient's information and meta data from the Dicom images and converted the Dicom images to a lossless jpg image format. After the conversion, each image finding was again verified by a radiologist and a medical technologist to reconfirm the correctness of the data.

Our created dataset contains 12,446 unique data within it in which the cyst contains 3,709, normal 5,077, stone 1,377, and tumor 2,283