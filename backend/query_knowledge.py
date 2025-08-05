from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from huggingface_llm import llm  # Your local HuggingFace pipeline wrapper

# Load embeddings and vectorstore
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

# Create retriever
retriever = db.as_retriever()

# Create RetrievalQA chain using your local llm
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

query = "What is this form about?"

result = qa.run(query)
print("Answer:", result)
