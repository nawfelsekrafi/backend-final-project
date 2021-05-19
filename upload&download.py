import pyrebase
from PIL import Image


config = {
    "apiKey": "AIzaSyBMDDOwcndSDbAzRlqYMZ4w0GWCJ_kLVHU",
    "authDomain": "backend-347db.firebaseapp.com",
    "databaseURL": "https://backend-347db-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "backend-347db",
    "storageBucket": "backend-347db.appspot.com",
    "messagingSenderId": "278802640563",
    "appId": "1:278802640563:web:5143a4bc0ef6997c9a8ac6"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "images/student1.jpg"
path_on_local = "./images/nawfel.jpg"
#storage.child(path_on_cloud).put(path_on_local)

#storage.child(path_on_cloud).download("./images/004.jpg")

#im = Image.open("./images/004.jpg")
#im.show()