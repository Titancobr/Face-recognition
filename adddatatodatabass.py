import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



ref = db.reference('students')

data = {
    "34245": {
        "Name": "Syed Ahmed",
        "Major": "CSE",
        "Starting_year": 2023,
        "total_attendance":17,
        "Year": 1,
        "Standings": "g",
        "last_attended_time": "2023-11-5 00:54:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)