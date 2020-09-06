from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import numpy as np
import pickle
import cv2
import os

app = Flask(__name__)
Bootstrap(app)
selected_model = 'modelConv.pkl' #can be model.pkl
model = pickle.load(open(selected_model,'rb'))
CLASSES = ['MESSY',"CLEAN"]

#routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if(selected_model=='modelConv.pkl'):
                img = cv2.resize(img, (64,64)).flatten()
            else:
                img = cv2.resize(img, (128,128)).flatten()
            img = np.asarray(img)
            prediction = model.predict([img])
            messy_clean=0
            if(prediction[0]>0.5):
                messy_clean=1
            class_name = CLASSES[messy_clean]
            result = {
                'class_name': class_name,
                'image_path': image_path,
            }
            return render_template('show.html',result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
