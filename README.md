# aiqom-export-model
The system has been built using AIQOM lab. We used tensorflowjs_wizrd to convert the model to keras model (h5) to use in in a webcam python code.

## Installations:
- [Anaconda Install](https://www.anaconda.com/products/individual)
- python==3.8.12
  ```bash
    conda create -n aiqom python=3.8
    conda activate aiqom
  ```
- tensorflow==2.8
  ```bash
    pip install tensorflow
  ``` 
- tensorflowjs[wizard]
  ```bash
    pip install tensorflowjs[wizard]
  ``` 
- openCV
  ```bash
  pip install opencv-python
  ``` 
- keras==2.6.*
  ```bash
  pip install keras==2.6.*
  ``` 

## Project setup
1. Clone the repo
```bash
git clone https://github.com/StallionDotAi/aiqom-export-model.git
```
2. Navigate to folder
```bash
cd aiqom-export-model
```
3. Insert step description here
```bash
wget 'INSERT_YOUR_MODELURL_HERE';wget 'INSERT_YOUR_WEIGHTSURL_HERE'
```
4. Install the required libraries.
```bash
pip3 install -r requirements.txt`
```
5. Convert the model to Keras model.
```bash
tensorflowjs_converter --input_format tfjs_layers_model --output_format keras my-model-1.json keras;python3 conv.py keras
```
6. Run the model on your webcam.
```bash
python webcam.py
```
