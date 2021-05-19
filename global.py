import json
#first of all we need to know what today is
from datetime import date
import datetime

today = date.today()
m = str(today.strftime("%m"))
d = str(today.strftime("%d"))
y = str(20) + str(today.strftime("%y"))
date= d + " " + m + " " + y
day_name= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
today = day_name[day]
print(today)
########################
#Connection with firebase
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':'https://backend-347db-default-rtdb.europe-west1.firebasedatabase.app/'
	})

ref = db.reference("/")
#post students info
with open("students_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
ref = db.reference("/")
#get all students in a specific day & store them in a list
#ki njiboubou student mel data base yjou sous form OrdereDic (dictionnaire key value) .. bch nejmou nest3mlouhom
#na3mlou appel lel function .items() . w mba3d na3mlou for loop 3la el dic hedha
#el value bch tji sous form dictionnair zeda (key value) so na3mlou value["days"]
#if today in value["days"] then append students list locally .. finally print the student list if it has members or
#print a message that say the opposite
students = []

q = ref.order_by_child("age").get()
for key,value in q.items():
	if today in value["days"]:
		students.append(value)

if(len(students) == 0):
	print("We dont have Students for this day")
else:
	for s in students:
		print(s["name"])

#lazem nzid imageList as a key in database
#lazem ntesti storage of firebase #############done
#lazem nchouf kifech ntelechargi les image fi folder #######done
#lazem na3mel for loop in recognition package . #########done

#import upload and download
import pyrebase

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
path_on_cloud = "images/"+ s["numero"]+"jpg"
storage.child(path_on_cloud).download("./images/"+img_title)