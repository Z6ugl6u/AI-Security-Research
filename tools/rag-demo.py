"""
rag-demo.py

RAG minimal :
Embed → Store → Retrieve → Generate

Installation :
pip install openai numpy

Variables d'environnement :
export OPENAI_API_KEY="sk-..."

Usage :
python rag-demo.py
"""

from openai import OpenAI
import numpy as np

# =========================
# CONFIG
# =========================

EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4.1-mini"

client = OpenAI()

# =========================
# BASE DE CONNAISSANCE
# =========================

documents = [
    "Paris est la capitale de la France.",
    
    "Linux est un système d'exploitation open source.",
    
    "Le protocole HTTP utilise généralement le port 80.",
    
    "Une injection SQL permet de manipuler une requête SQL.",
    
    "Le chiffrement AES est symétrique.",
]

# =========================
# EMBEDDINGS
# =========================

def get_embedding(text):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response.data[0].embedding


print("[+] Génération des embeddings...")

document_embeddings = []

for doc in documents:
    embedding = get_embedding(doc)
    document_embeddings.append(embedding)

# =========================
# SIMILARITÉ COSINUS
# =========================

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# =========================
# RETRIEVAL
# =========================

def retrieve(query, top_k=2):

    query_embedding = get_embedding(query)

    scores = []

    for i, doc_embedding in enumerate(document_embeddings):

        score = cosine_similarity(query_embedding, doc_embedding)

        scores.append((documents[i], score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:top_k]


# =========================
# GENERATION
# =========================

def generate_answer(query, context_docs):

    context = "\n".join(context_docs)

    prompt = f"""
Contexte :
{context}

Question :
{query}

Réponds uniquement avec les informations du contexte.
"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# =========================
# MAIN
# =========================

if __name__ == "__main__":

    query = input("\nQuestion : ")

    print("\n[+] Recherche des documents pertinents...\n")

    results = retrieve(query)

    for doc, score in results:
        print(f"Score: {score:.4f}")
        print(f"Doc: {doc}\n")

    context_docs = [doc for doc, _ in results]

    print("[+] Génération de la réponse...\n")

    answer = generate_answer(query, context_docs)

    print("Réponse :\n")
    print(answer)