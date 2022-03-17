# aiqom-export-model
The system has been built using AIQOM lab. We used tensorflowjs_wizrd to convert the model to keras model (h5) to use in in a webcam python code.

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
tensorflowjs_converter --input_format tfjs_layers_model --output_format keras model.json keras.h5
```
6. Run the model on your webcam.
```bash
python webcam.py
```
