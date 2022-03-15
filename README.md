# aiqom-export-model
The system has been built using AIQOM lab. We used tensorflowjs_wizrd to convert the model to keras model (h5) to use in in a webcam python code.

# Instructions
1. Clone the repo

`git clone https://github.com/StallionDotAi/aiqom-export-model.git`

2. Navigate to Folder

`cd aiqom-export-model`

3. Insert step description here

`curl 'INSERT_YOUR_MODELURL_HERE'`

4. 

`pip3 install -r requirements.txt`

5. 

`tensorflowjs_converter --input_format tfjs_layers_model --output_format keras model.json keras;python3 conv.py keras`

6. 

`python webcam.py`

