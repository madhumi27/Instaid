from flask import Blueprint, render_template, request, send_from_directory
from .app_functions import ValuePredictor, pred
import os
from werkzeug.utils import secure_filename

prediction = Blueprint('prediction', __name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

dir_path = os.path.dirname(os.path.realpath(__file__))



@prediction.route('/predictdiab', methods=["POST",'GET'])

def predict_diab():

    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result, page = ValuePredictor(to_predict_list) 
        insulin=request.form['Insulin']
        return render_template("resultdiab.html", prediction=result,Insulin=insulin)
    else:
        return render_template('base.html')     

@prediction.route('/predictliver', methods=["POST",'GET'])

def predict_liver():

    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result, page = ValuePredictor(to_predict_list) 
        return render_template("resultliver.html", prediction=result)
    else:
        return render_template( 'base.html')        

@prediction.route('/predictheart', methods=["POST",'GET'])

def predict_heart():

    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result, page = ValuePredictor(to_predict_list) 
        rbp = request.form['trestbps']
        return render_template("resultheart.html", prediction=result,rbp=rbp)
    else:
        return render_template( 'base.html')        

@prediction.route('/predictstroke', methods=["POST",'GET'])

def predict_stroke():

    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result, page = ValuePredictor(to_predict_list) 
        glu=request.form['avg_glucose_level']
        tens=request.form['hypertension']
        return render_template("resultstroke.html", prediction=result,glu=glu,tens=tens)
    else:
        return render_template( 'base.html')        

@prediction.route('/predictkidney', methods=["POST",'GET'])

def predict_kidney():

    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result, page = ValuePredictor(to_predict_list) 
        return render_template("resultkidney.html", prediction=result)
    else:
        return render_template( 'base.html')        


@prediction.route('/upload', methods=['POST','GET'])

@prediction.route('/predict')

def predict():
    return render_template( 'base.html')

def upload_file():
    if request.method=="GET":
        return render_template('pneumonia.html', title='Pneumonia Disease')
    else:
        file = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath,'uploads',  secure_filename(file.filename))
        file.save(file_path)
        indices = {0: 'Normal', 1: 'Pneumonia'}
        result = pred(file_path)

        if result>0.5:
            label = indices[1]
            accuracy = result * 100
        else:
            label = indices[0]
            accuracy = 100 - result
        return render_template('deep_pred.html', image_file_name=file.filename, label = label, accuracy = accuracy)

@prediction.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)