# FILESTORAGE
A server with a file storage that implements a functions listed below:

1. List all the files
2. Upload a file
3. Delete a file by providing its name


## Production server building
To quick launch the production version we use the Docker container on a **python2.8-alpine** image with **nginx** installed additionally.
uWSGI is used for serving Flask application. The API production server listens to a 80 port.


### The very first launch

For building an image at the first time:

```
make build
```


### To stop the server

```
make stop
```


### To start server again

```
make start
```


## Default configuration

Initially, the maximum file upload size is limited by default to 50 MB.
It is also allowed to upload all types of files.
If necessary, we can change these settings in the file **./filestorage.py** file.


## Versioning

Sometimes we need to change a functionality, so the prevoius functionally is totally breaks. We must to provide a reliable and efficient service for users. That is why we always should be sure that our API is up-to-date and bug-free. This is why we use versioning in our API.

### Why Versioning is Important
1. **Backwards Compatibility**: By versioning our API, we are able to ensure that previous versions of the API will continue to work as expected. This means that if a user is using an older version of the API (i.e. an older version ov CLI application), they will not be affected by any changes made to the newer versions.

2. **Testing**: Versioning allows us to test new features and changes in a controlled environment before releasing them to the public. This means that we can ensure that the new version of the API is stable and reliable before making it available to our users.

### How to implement versioning in this API

One way to achieve this is by creating a new folder for the new version within the **api** directory. For example, if we are creating version 2 of the API, we would create a new folder named "v2" within the *api* directory, and then we would implement all of the new functionality and changes. Additionally we would add some directives to ./filestorage.py file.
This allows us to keep the new version separate from the previous version, making it easy to maintain and test. Additional we would create a new version of CLI that will work with a new version of API.



## About this API

### Why Python?
According to [StackOverflow analysis](https://survey.stackoverflow.co/2022/#technology-most-popular-technologies), Python is one of the fastest-growing programming languages nowadays. More and more libraries are being developed for a wide variety of needs. This makes Python a great tool for solving a wide range kinds of problems.

### Why Flask?
Flask developers call it a "microframework", what means that the core is simple but extensible.
For such simple tasks as a file storage service, it is best suited: all the necessary functionality is present without overloading with unnecessary modules.

### What may be improved
Now, for simplicity purpose, service displays only file names. In order to increase the convenience of working with service, we can also show the size of files, the date of creation, the author, and so on.
We can also add a file filter by passing various parameters.


## Developing mode

For developing purpose we should install [Flask](https://flask.palletsprojects.com/en/2.2.x/) and also [pipenv](https://pipenv.pypa.io/en/latest/) for dependency managing.
Then from the application root directory run:
```
./entrypoint.sh
```
Developing server works on 5000 port.

### Testing a requests

For testing we can use a [curl](https://curl.se/) library (change port to 5000 on a developing server): 

#### File listing
```
curl http://localhost:80/v1/files
```
#### File uploading
```
curl -X POST -F file=testfile.txt http://localhost:80/v1/files
```
#### File deleting
```
curl -X DELETE http://localhost:80/v1/files/testfile.txt
```



The requests to the server without a version mark references to the last version of the API. So as current last version is v1, the request:
```
curl http://localhost/files
```
if the same as:
```
curl http://localhost/v1/files
```