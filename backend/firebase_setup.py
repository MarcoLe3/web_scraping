import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collections = db.collections()

print("Collections in Firestore:")
for col in collections:
    print(col.id)
