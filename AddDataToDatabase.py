import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-system-14636-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "43307":
        {
            "name": "Fazal",
            "major": "Graduation",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-2-11 00:54:34"
        },
    "44881":
        {
            "name": "Dulquer",
            "major": "Bussiness",
            "starting_year": 2018,
            "total_attendance": 10,
            "standing": "G",
            "year": 5,
            "last_attendance_time": "2023-2-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
