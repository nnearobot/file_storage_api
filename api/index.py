import os
from flask import Flask, jsonify, request
from api.model.messages import Message
from werkzeug.utils import secure_filename
import http.client

UPLOAD_FOLDER = 'files'
MAX_CONTENT_LENGTH = 16 * 1000 * 1000
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH



# Root of the app
@app.route("/")
def filestorage():
    return Message.HELLO.value




# List all files
@app.route('/files', methods=['GET'])
def get_filelist():
    dir_list = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify(dir_list)




# Upload file
@app.route('/files', methods=['POST'])
def upload_file():
    # check if the request has the file:
    if 'file' not in request.files:
        return Message.UNKNOWN_FILE.value, http.client.BAD_REQUEST
    
    file = request.files['file']
    if not file or file.filename == '':
        return Message.UNKNOWN_FILE.value, http.client.BAD_REQUEST

    filename = secure_filename(file.filename)
    ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    if ext not in ALLOWED_EXTENSIONS:
        return Message.BAD_EXTENTION.value.format(ext), http.client.UNPROCESSABLE_ENTITY

    dir_list = os.listdir(app.config['UPLOAD_FOLDER'])
    if filename in dir_list:
        return Message.FILE_EXISTS.value.format(filename), http.client.UNPROCESSABLE_ENTITY

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return Message.UPLOADED_SUCCESSFULLY.value.format(filename), http.client.CREATED





# Delete file
@app.route('/files/<name>', methods=['DELETE'])
def delete_file(name):
    if name == "":
        return Message.UNKNOWN_FILENAME.value, http.client.BAD_REQUEST

    dir_list = os.listdir(app.config['UPLOAD_FOLDER'])
    if name not in dir_list:
        return Message.NOT_EXIST.value.format(name), http.client.NOT_FOUND

    path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    os.remove(path)
    return Message.DELEATED.value.format(name), http.client.NO_CONTENT