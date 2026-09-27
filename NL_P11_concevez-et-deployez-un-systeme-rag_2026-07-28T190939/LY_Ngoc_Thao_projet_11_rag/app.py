from pathlib import Path
from dotenv import load_dotenv

import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

VECTORSTORE_PATH = Path("vectorstore/faiss_versailles")


@st.cache_resource
def load_vectorstore():
    embeddings = MistralAIEmbeddings(model="mistral-embed")

    return FAISS.load_local(
        str(VECTORSTORE_PATH),
        embeddings,
        allow_dangerous_deserialization=True
    )


def retrieve_context(vectorstore, question, k=4):
    docs = vectorstore.similarity_search(question, k=k)

    context = "\n\n".join([
        f"""
Titre : {doc.metadata.get("title")}
Date : {doc.metadata.get("date")}
Ville : {doc.metadata.get("city")}
Description : {doc.page_content}
URL : {doc.metadata.get("url")}
"""
        for doc in docs
    ])

    return context, docs


def generate_answer(question, context):
    llm = ChatMistralAI(
        model="mistral-small-latest",
        temperature=0.2
    )

    prompt = ChatPromptTemplate.from_template("""
Tu es un assistant spécialisé dans la recommandation d'événements culturels à Versailles.

Réponds uniquement à partir du contexte fourni.
Si tu ne trouves pas d'événement pertinent, dis-le clairement.
Propose une réponse naturelle, concise et utile.

Contexte :
{context}

Question utilisateur :
{question}

Réponse :
""")

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content


st.set_page_config(
    page_title="Assistant culturel Versailles",
    page_icon="🎭",
    layout="centered"
)

st.title("🎭 Assistant culturel - Versailles")
st.write("Posez une question pour obtenir des recommandations d'événements culturels à Versailles.")

question = st.text_input(
    "Votre question",
    placeholder="Exemple : Je cherche un concert à Versailles"
)

if st.button("Rechercher"):
    if not question.strip():
        st.warning("Veuillez saisir une question.")
    else:
        with st.spinner("Recherche des événements pertinents..."):
            vectorstore = load_vectorstore()
            context, docs = retrieve_context(vectorstore, question)
            answer = generate_answer(question, context)

        st.subheader("Réponse du chatbot")
        st.write(answer)

        st.subheader("Événements retrouvés")
        for doc in docs:
            st.markdown(f"**{doc.metadata.get('title')}**")
            st.write(f"Date : {doc.metadata.get('date')}")
            st.write(f"Ville : {doc.metadata.get('city')}")
            if doc.metadata.get("url") and str(doc.metadata.get("url")) != "nan":
                st.write(doc.metadata.get("url"))
            st.divider()