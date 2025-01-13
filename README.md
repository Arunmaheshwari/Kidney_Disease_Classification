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



## 1. Data 

I am using data from the kaggle named "ct-kidney-dataset-normal-cyst-tumor-and-stone"
```bash
https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone
```
As of now i have stored data in Google drive, and by making function we are getting data from there in zip file and then we unzip the data.

## 2. Base Model

I am using VGG16 Model, i have taken this model from the tensorflow and here i have freeze the all the layers excepted full connected Neural layers and used IMAGENET weights.


## 3. Training

Here i have have trained model by using keras library on my dataset and used pretrained VGG16 model. and stored in inside the artifacts folder named model.h5.


## 4. Model evaluation

I  evaluated the performance of the model by using
    
    Mlflow and Dagshub

here by changing the the parameter, data, pretrained model as well, i can evaluate the performace of the model.

By using Mlflow i can compare the different model performance as well.








### Creation for file and way of work i have done
How i have completed this project, steps and workflow i have follow while creating the multiple file.
## 1. Data Ingestion

Ingested data from the google drive and stored in zip file and the unzip it.

## 2. Prepare base model

I am using VGG16 Model, i have taken this model from the tensorflow and here i have freeze the all the layers excepted full connected Neural layers and used IMAGENET weights.




## 3. Training

Here i have have trained model by using keras library on my dataset and used pretrained VGG16 model. and stored in inside the artifacts folder named model.h5.


## 4. Model evaluation

I  evaluated the performance of the model by using
    
    Mlflow and Dagshub

here by changing the the parameter, data, pretrained model as well, i can evaluate the performace of the model.

By using Mlflow i can compare the different model performance as well.

Here i also got scores.json file, which tells me that most recent model evaluation performance.



## 5. Integration of DVC

Ingegrated DVC to ensure that again and again same data file will not excecute.

command for running dvc -
```bash
dvc init
```

```bash
dvc repro
```










## About Dataset

# Context
CT KIDNEY DATASET: Normal-Cyst-Tumor and Stone

# Content
The dataset was collected from PACS (Picture archiving and communication system) from different hospitals in Dhaka, Bangladesh where patients were already diagnosed with having a kidney tumor, cyst, normal or stone findings. Both the Coronal and Axial cuts were selected from both contrast and non-contrast studies with protocol for the whole abdomen and urogram. The Dicom study was then carefully selected, one diagnosis at a time, and from those we created a batch of Dicom images of the region of interest for each radiological finding. Following that, we excluded each patient's information and meta data from the Dicom images and converted the Dicom images to a lossless jpg image format. After the conversion, each image finding was again verified by a radiologist and a medical technologist to reconfirm the correctness of the data.

Our created dataset contains 12,446 unique data within it in which the cyst contains 3,709, normal 5,077, stone 1,377, and tumor 2,283