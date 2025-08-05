# store_form.py
from backend.firebase_setup import db

form_data = {
    "form_name": "pizza_order_form",
    "fields": {
        "custname": "text",
        "custtel": "tel",
        "custemail": "email",
        "size": ["small", "medium", "large"],
        "topping": ["cheese", "onion", "bacon"],
        "delivery": "time"
    }
}

# Save to Firestore
doc_ref = db.collection("forms").document("pizza_order_form")
doc_ref.set(form_data)

print("Form structure saved to Firestore")
