from enum import Enum

class Message(Enum):
    HELLO = "Hello! This is a simple file storage."
    UNKNOWN_FILE = "Unknown file. Please check the request and try again"
    UNKNOWN_FILENAME = "Unknown file name. Please check the request and try again"
    FILE_EXISTS = "File named {} already exists in the storage. Please rename the file and try to upload again."
    BAD_EXTENTION = "File with extention {} does not allowed."
    UPLOADED_SUCCESSFULLY = "File {} uploaded successfully"
    NOT_EXIST = "File {} does not exist. Please ensure the file name and try again."
    DELEATED = "File {} successfully deleted"
    TOO_LARGE = "File {} is too large. Allowed file size limit is {}M"