import streamlit as st
from chatbot_model import *
from google.cloud import translate_v2 as translate

# Fonction de traduction
def traduire_texte(texte, langue_source, langue_cible):
    client = translate.Client()
    resultat = client.translate(texte, source_language=langue_source, target_language=langue_cible)
    return resultat['translatedText']

# Barre latérale (side page) pour entrer les données liées à la langue
st.sidebar.header("Options")

# Ajouter des options pour la couleur de discussion pour chaque rôle
couleur_user = st.sidebar.color_picker('Couleur Utilisateur', '#0000FF')
couleur_chatbot = st.sidebar.color_picker('Couleur ChatBot', '#FF0000')

# Ajouter des options pour les langues source et cible
langue_source = st.sidebar.selectbox("Sélectionner la langue source", ["en", "fr"])
langue_cible = st.sidebar.selectbox("Sélectionner la langue cible", ["en", "fr"])

# Page principale (main page) pour la barre d'entrée et l'historique de la discussion
st.title("⚕️ CareBot - Emergency Service Chat")

# Liste d'entrées de chat
chat_entries = []

# Barre d'entrée pour que l'utilisateur pose des questions
question_input = st.text_input("Entrez votre question")

# Bouton pour l'urgence
rerun_button = st.button("⚠️ Urgence", help="Cliquez pour le service d'urgence")

if question_input:
    # Traduire la question si la langue source est différente de la langue cible
    if langue_source != langue_cible:
        question_input = traduire_texte(question_input, langue_source, langue_cible)
    
    response = chatbot_response(question_input)

    # Ajouter la question de l'utilisateur à la liste des entrées de chat
    chat_entries.append(("Utilisateur", question_input))
    # Ajouter la réponse du chatbot à la liste des entrées de chat
    chat_entries.append(("ChatBot", response))
else:
    response = None

if rerun_button:
    response = chatbot_response(question_input)

    # Ajouter la réponse d'urgence du chatbot à la liste des entrées de chat
    chat_entries.append(("ChatBot (Urgence)", response))
else:
    pass

# Afficher l'historique de la discussion mis à jour avec des couleurs différentes
for role, message in chat_entries:
    if role == "Utilisateur":
        st.write(f'<p style="color:{couleur_user}">{role}: {message}</p>', unsafe_allow_html=True)
    elif role == "ChatBot":
        st.write(f'<p style="color:{couleur_chatbot}">{role}: {message}</p>', unsafe_allow_html=True)
    else:
        st.write(f'<p style="color:{couleur_chatbot}">{role}: {message}</p>', unsafe_allow_html=True)

# Afficher la réponse actuelle dans le format de discussion
if response:
    # Traduire la réponse si la langue source est différente de la langue cible
    if langue_source != langue_cible:
        response = traduire_texte(response, langue_cible, langue_source)

    # Afficher la réponse du chatbot avec la couleur appropriée
    st.write(f'<p style="color:{couleur_chatbot}">ChatBot: {response}</p>', unsafe_allow_html=True)
