import json
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import UI.Windo as ui
import BL.IdentifyModel as idt

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, "DAL/dataset/clientsImage/")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
menu= ui.Menu()

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

'''
def orderEndline_dict(d):
    for kay in d.keys():
        if (type(l[i_evar][kay]) == str):


def orderEndline(l):
    for i_evar in range(len(l)):
        for kay in l[i_evar].keys():
            if(type(l[i_evar][kay])== str):
                l[i_evar][kay] = l[i_evar][kay].replace("\n", "<br/>")
            elif(type(l[i_evar][kay])== dict):
                for kay2 in l[i_evar].keys():
                    if (type(l[i_evar][kay]) == str):
                        l[i_evar][kay][kay2] = l[i_evar][kay][kay2].replace("\n", "<br/>")
            else: l[i_evar][kay] =orderEndline(l[i_evar][kay])
'''

@app.route("/")
def hello_world():
    return ""#menu.mainPageAsStr()


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print("UploadImageFunc")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            try:
                result = idnifyObject(filename)
                if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
                    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                else:
                    print("The file does not exist")

                data = {"status": True, "data": {"name": result, "hebrewName": menu.translateNameFruit2hebrew(result)}}
                return json.dumps(data) #return "{\"status\":true,\"data\":{\"name\":\""+result+"\"}}"
            except:
                return "{\"status\":false}"
    return "{}"


@app.route('/recipients/<name>')
def download_recipints(name):
    if request.method == 'GET':
        # check if the post request has the file part
        '''
        if name==None or name=="":
            flash('No file part')
            return redirect(request.url)
            '''
        try:
            l_recipients = menu.getRecipients(menu.translateNameFruit2hebrew(name))
            #orderEndline(l_recipients)
            data= {"status": True, "data": l_recipients}
            return json.dumps(data) #"{\"status\":true,\"data\":\""+str(l_recipients)+"\"}"
        except:
            return "{\"status\":false}"
    return "{}"

@app.route('/data/<name>')
def getData(name):
    if request.method == 'GET':
        # check if the post request has the file part
        '''
        if name==None or name=="":
            flash('No file part')
            return redirect(request.url)
            '''
        try:
            l_data = menu.getDataFruites(menu.translateNameFruit2hebrew(name))
            data= {"status": True, "data": l_data}
            return json.dumps(data) #"{\"status\":true,\"data\":\""+str(l_recipients)+"\"}"
        except:
            return "{\"status\":false}"
    return "{}"

@app.route('/cosharot/<name>')
def getCosharotData(name):
    if request.method == 'GET':
        # check if the post request has the file part
        '''
        if name==None or name=="":
            flash('No file part')
            return redirect(request.url)
            '''
        try:
            l_data = menu.getData_cosharot(menu.translateNameFruit2hebrew(name))
            data= {"status": True, "data": l_data}
            return json.dumps(data) #"{\"status\":true,\"data\":\""+str(l_recipients)+"\"}"
        except:
            return "{\"status\":false}"
    return "{}"

# http://178.62.223.209:5000/upload'
