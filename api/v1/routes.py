from api.v1.messages import Message
import os
from flask import Blueprint, current_app, jsonify, request
import werkzeug.exceptions
from werkzeug.utils import secure_filename
import http.client


api = Blueprint('api', __name__)

upload_folder = 'files' # this can be changed for another version of API
maxFileSize = current_app.config['MAX_CONTENT_LENGTH']
allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']

# Root of the app
@api.route("/")
def filestorage():
    return Message.HELLO.value


# List all files
@api.route('/files', methods=['GET'])
def get_filelist():
    dir_list = os.listdir(upload_folder)
    return jsonify(dir_list)


# Upload file
@api.route('/files', methods=['POST'])
def upload_file():
    # check if the request has the file:
    if 'file' not in request.files:
        return Message.UNKNOWN_FILE.value, http.client.BAD_REQUEST
    
    file = request.files['file']
    if not file or file.filename == '':
        return Message.UNKNOWN_FILE.value, http.client.BAD_REQUEST

    filename = secure_filename(file.filename)
    ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    if len(allowed_extensions) > 0 and ext not in allowed_extensions:
        return Message.BAD_EXTENTION.value.format(ext), http.client.UNPROCESSABLE_ENTITY

    dir_list = os.listdir(upload_folder)
    if filename in dir_list:
        return Message.FILE_EXISTS.value.format(filename), http.client.FORBIDDEN

    try:
        file.save(os.path.join(upload_folder, filename))
        return Message.UPLOADED_SUCCESSFULLY.value.format(filename), http.client.CREATED
    except werkzeug.exceptions.RequestEntityTooLarge:
        fileSizeM = maxFileSize / (1024 * 1024)
        api.logger.warning('fileSizeM: %d', fileSizeM)
        return Message.TOO_LARGE.value.format(filename, fileSizeM), http.client.REQUEST_ENTITY_TOO_LARGE
    


# Delete file
@api.route('/files/<name>', methods=['DELETE'])
def delete_file(name):
    if name == "":
        return Message.UNKNOWN_FILENAME.value, http.client.BAD_REQUEST

    dir_list = os.listdir(upload_folder)
    if name not in dir_list:
        return Message.NOT_EXIST.value.format(name), http.client.NOT_FOUND

    path = os.path.join(upload_folder, name)
    os.remove(path)
    return Message.DELEATED.value.format(name), http.client.NO_CONTENT