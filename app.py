from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from botocore.exceptions import NoCredentialsError
import boto3
import os
import botostuff

bucket_name = 'my-very-useful-bucket-2025'

foodconfdict = {}

UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def python_function(filename):
    foodconfdict.clear()
    image_recognition_client = boto3.client('rekognition')



    response = image_recognition_client.detect_labels(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': filename}})
    # print(response)
    labels = response['Labels']
    for i in labels:
        print(f"{i['Name']} : Confidence level: {i['Confidence']}")
        foodconfdict.update({i['Name']:i['Confidence']})


@app.route("/")
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if "file" not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == "":
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

        file.save(filepath)



        s3 = boto3.client('s3')
        try:
            s3.upload_file(filepath, bucket_name, filename)
            print(f"{filename} uploaded")
            python_function(filename)
            return f"{foodconfdict[0]}"


        except NoCredentialsError:
            return "Access Denied", 403

    return "Invalid file type", 400

if __name__ == '__main__':
    app.run(debug=True, port=8000)