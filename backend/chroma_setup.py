import firebase_admin
from firebase_admin import credentials, firestore

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. Init Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 2. Fetch scraped forms text from Firestore
docs = db.collection("forms").stream()

all_texts = []
for doc in docs:
    data = doc.to_dict()
    form_name = data.get("form_name", "")
    fields = data.get("fields", {})

    if fields:
        # Convert the fields dict into a readable string
        field_texts = [f"{key}: {value}" for key, value in fields.items()]
        combined_text = f"Form Name: {form_name}\n" + "\n".join(field_texts)
        all_texts.append(combined_text)

if not all_texts:
    raise ValueError("No text fetched from Firebase! Check your collection and document fields.")

big_text = "\n\n".join(all_texts)
documents = [Document(page_content=big_text)]

# 3. Split docs for Chroma
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(documents)

# 4. Create embeddings and Chroma DB
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(split_docs, embeddings, persist_directory="chroma_db")
vectorstore.persist()

print("Chroma DB created with Firebase data")
