## ROOM CLEANLINESS CLASSIFIER
> An Image-Classification Project - Room Cleanliness Classifier is a Machine Learning based web application that take input a picture/photograph of a room's inner surroundings and figures out if the room is in clean condition or messy condition. (Involves Machine Learning, Deep Learning and Flask for backend & deployment)

## Content
* [Overview of the Project](#overview) 
    * [Deployed web application address/link](#deployed-web-app) 
    * [What is it all about?](#what-is-it-all-about)
* [Technical details](#technical-details) 
    * [The tech-stack used in the development of the project](#tech-stack) 
    * [How to download/clone and execute the Project (including server-side scripts) on your machine](#how-to-execute-on-your-machine) 
    * [Prediction of Test images](#prediction-of-test-images)
    * [About the ipynb notebooks](#about-the-ipynb-notebooks)
    * [Use cases](#use-cases)
    * [Accuray and Future Scope](#accuracy-and-future-scope)

# Overview

## Deployed Web App
The working version of this ML based web-app is deployed on Heroku platform. Go to [https://room-cleanliness-classifier.herokuapp.com/](https://room-cleanliness-classifier.herokuapp.com) to have a look.


## What is it all about?
This project is made in order to classify the image input of a room's inner surroundings into two categories - one of which is `Messy` and the other is `Clean`. This can helpful in the automation of Robotic cleaners in an efficient manner.
This project involves the implementation of Logistic Regression machine learning algorithm with the neural network mindset simulating the forward propagation and backward propagation. Also, I have trained the models using various scikit-learn python library implementations. And last but not the least, I have trained a CNN model using Tensorflow and Keras and studied the performances of all the mentioned models.

# Technical details

## Tech Stack
The technologies used to develop this web applications are 
* Logistic Regression (Core Machine Learning)
* scikit-learn
* Tensorflow Keras API
* HTML
* CSS
* Flask micro-framework

#### Brief Information
> Logistic Regression algorithm is applied with the implementation of Forward Propagation and Bachward propagation, resembling the working of a perceptron.

> Various ML classification algorithms via sklearn have been applied to make the predictions for comparison with CNN and Logistic Regression implementation.

> Tensorflow backed Keras API is used to build a sequencial Convolutional Neural Network model for image classification.

> HTML, CSS and Bootstrap have been used in front-end for structuring and designing of the project. 

> Flask is used to build the web application server-script, connect all the web pages appropriately and writing the logic part of the project.


## How to execute on your machine

> Follow/Understand the steps to execute/run the project on your machine.

* Download and extract the zip bundle of the project or clone the project using git cloning commands.


* Download and install python if your system doesn’t have python. It is assumed that you are downloading the project on the python-installed machine.

* Install the Flask (and the dependencies) by executing the following command
```python
pip install flask
```

* Now, simply run the following command to run the web application on your browser on port `5000`	
```python
python app.py
```
If all the dependencies are satisfied, then you are good to go. The application would run successfully. :)

* Verify the deployment by navigating to your server address in your preferred browser.
```python
127.0.0.1:5000
```

## Prediction of Test images
![The test image prediction](static/img/capture1.jpg)
![](static/img/capture2.jpg)

## About the ipynb notebooks

These include the main Machine Learning codes with proper documentations as required. I hope there would not be any problem in understanding any line of the code. There are two notebooks - One with the Logistic Regression implementation and the other with the sklearn models and CNN model.

In case, the ipynb notebook fails to open in github platform, download the notebook and open via Jupyter or Google Colaboratory platform. You can also use the https://nbviewer.jupyter.org/ platform to render the jupyter notebook online using the github link (github url of notebook).


## Use cases

> Automation of House keeping robotic processes

> The models can also be trained on the scenes of public places and amusement parks and it may be then used for automation of keeping the public places clean


## Accuracy and future scope

> In the implementation of Logistic Regression, the model gives 59.375% Test Dataset accuracy after 2500 iterations.

> In the sklearn algorithms, the models perform roughly in the range of 53% to 60% accuracy on evaluation.

> In the Convolutional Neural Net model, it gives 78.12% Test Dataset accuracy after 5 epochs.

> The models can have a huge improvements in terms of performance using the pretrained Incention or VGG models via Transfer Learning.