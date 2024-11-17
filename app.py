import json
import os
from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename
import controller.Windo as ui

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, "DAL/dataset/clientsImage/")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
menu = ui.Menu()


@app.after_request
def after_request(response):
    response.access_control_allow_origin = "*"
    return response


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def idnifyObject(nameFile):
    name = menu.idetifyImage(nameFile)
    return name


@app.route("/")
def hello_world():
    print("when it enter here?")
    return ""  # menu.mainPageAsStr()


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print("UploadImageFunc")
    if request.method != 'POST':
        return "{}"
    try:
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            raise
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            raise Exception('No selected file')
        if not(file and allowed_file(file.filename)):
            raise Exception("file not allowed")
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        result = idnifyObject(filename)
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            print("The file does not exist")
        data = {"status": True, "data": {"name": result, "hebrewName": menu.translateNameFruit2hebrew(result)}}
        return json.dumps(data)
    except Exception as e:
        print(e)
        data = {"status": False, "data": {"name": "ERROR", "details": e, "data": redirect(request.url)}}
        return json.dumps(data)
    except:
        data = {"status": False, "data": None}
        return json.dumps(data)



@app.route('/recipients/<name>')
def download_recipints(name):
    # print("get recipients function")
    if request.method == 'GET':
        try:
            page_number =request.args.get("pageNumber")
            page_size = request.args.get("pageSize")
            l_recipients, pages = menu.getRecipients(name, page_number, page_size)
            data = {"status": True, "data": {"data": l_recipients, "pages":pages}}
            return json.dumps(data)
        except:
            data = {"status": False, "data": None}
            return json.dumps(data)
    return "{}"


@app.route('/data/<name>')
def getData(name):
    if request.method == 'GET':
        try:
            l_data = menu.getDataFruites(menu.translateNameFruit2hebrew(name))
            data = {"status": True, "data": l_data}
            return json.dumps(data)
        except:
            data = {"status": False, "data": None}
            return json.dumps(data)
    return "{}"


@app.route('/cosharot/<name>')
def getCosharotData(name):
    if request.method == 'GET':
        try:
            page_number =request.args.get("pageNumber")
            page_size = request.args.get("pageSize")

            l_data = menu.getData_cosharot(menu.translateNameFruit2hebrew(name))
            pages = 1
            data = {"status": True, "data": {"data": l_data, "pages": pages}}
            return json.dumps(data)
        except:
            return "{\"status\":false}"
    return "{}"

@app.route('/cosharot/one/<index>')
def get_oneCosharot(index):
    print("get cosharot function")
    if request.method == 'GET':
        try:
            cashroot = menu.getCosharotByIndex(index)
            data = {"status": True, "data": {"item": cashroot}}
            return json.dumps(data)
        except:
            data = {"status": False, "data": None}
            return json.dumps(data)
    return "{}"
@app.route('/recipient/<index>')
def download_oneRecipint(index):
    # print("get recipients function")
    if request.method == 'GET':
        try:
            recipient = menu.getRecipintByIndex(index)
            data = {"status": True, "data": {"item": recipient}}
            return json.dumps(data)
        except:
            data = {"status": False, "data": None}
            return json.dumps(data)
    return "{}"


# http://178.62.223.209:5000/upload'
