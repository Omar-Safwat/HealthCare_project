from flask import Flask, request, render_template, send_file, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import json
from dataset_validation import validate_cols #Omar's module to validate uploaded dataset

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download-template', methods=['POST'])
def download_csv_template():
    return send_file('template.csv',
                     mimetype='text/csv',
                     attachment_filename='template.csv',
                     as_attachment=True)

#every upload file will be saved with this name
global uploaded_doc_name
uploaded_doc_name = 'downloaded.csv'

# Validate dataset
validation_output = validate_cols(uploaded_doc_name) #returns a string object to be displayed to the user. Either success of failure.


@app.route('/upload-dataset', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(uploaded_doc_name))
        return redirect(url_for('uploaded_successfully'))

@app.route('/uploaded-successfully')
def uploaded_successfully():
    return render_template('redirect_upload_success.html')

# save predicted file as csv and update name
global predicted_file_name_csv
predicted_file_name_csv = 'test_prediction.csv'


@app.route('/download-prediction', methods=['POST'])
def download_csv_predicted():
    return send_file(predicted_file_name_csv,
                     mimetype='text/csv',
                     attachment_filename=predicted_file_name_csv,
                     as_attachment=True)

if  __name__== '__main__':
    app.run(port=8082, debug=True)
