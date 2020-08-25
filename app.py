from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import numpy as np
import pickle
import cv2
import os

app = Flask(__name__)
Bootstrap(app)
model = pickle.load(open('model.pkl','rb'))
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
            img = cv2.resize(img, (128,128)).flatten()
            img = np.asarray(img)
            prediction = model.predict([img])
            class_name = CLASSES[int(prediction[0])]
            result = {
                'class_name': class_name,
                'image_path': image_path
            }
            return render_template('show.html',result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
