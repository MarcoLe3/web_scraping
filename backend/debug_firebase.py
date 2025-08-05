import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

docs = db.collection("forms").stream()

for doc in docs:
    print(f"Doc ID: {doc.id}")
    data = doc.to_dict()
    print("Fields:")
    for k, v in data.items():
        print(f"  {k}: {v}")
    print("-" * 20)