#installiamo le librerie necessarie nel terminale: pip install transformers torch streamlit
#per utilizzare questo codice, è necessario avere Python installato sul proprio computer e le librerie Transformers, Torch e Streamlit.
#pip install deep-translator: questa libreria è necessaria per tradurre il testo in inglese, se l'utente inserisce un testo in una lingua diversa dall'inglese.
#per eseguire l'applicazione, utilizziamo il comando: python -m streamlit run app.py
#pip install langdetect: questa libreria è necessaria per rilevare la lingua del testo inserito dall'utente, in modo da poterlo tradurre correttamente se non è in inglese.

from langdetect import detect
from deep_translator import GoogleTranslator 
from config import emoji #per associare le emozioni a delle emoji, rendendo l'interfaccia più visiva e intuitiva
from config import traduzioni #per supportare più lingue nell'interfaccia, rendendo l'applicazione accessibile a un pubblico più ampio
import streamlit as st #per realizzare l'interfaccia grafica
from transformers import pipeline #per utilizzare i modelli di intelligenza artificiale
import pdfplumber #per estrarre il testo dai file PDF
from config import stelle 
import pandas as pd


classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base") 
#carichiamo il modello di intelligenza artificiale per l'analisi delle emozioni
#il tipo di compito: "text-classification"
#il nome del modello: "j-hartmann/emotion-english-distilroberta-base"

#creiamo l'interfaccia grafica con Streamlit
#Streamlit è una libreria Python che ti permette di creare interfacce web in modo semplicissimo, senza dover sapere HTML, CSS o JavaScript.
lingua_selezionata = st.sidebar.selectbox("Choose language", options=["🇮🇹 Italiano", "🇬🇧 English", "🇩🇪 Deutsch", "🇫🇷 Français", "🇪🇸 Español", "🇵🇹 Português"], index=0, key="lingua") #creiamo un menu a tendina per scegliere la lingua dell'interfaccia
lingua_interfaccia = lingua_selezionata.split()[1] #estraiamo la lingua selezionata dall'utente
titolo = st.title(traduzioni[lingua_interfaccia]["titolo"])
st.write(traduzioni[lingua_interfaccia]["descrizione"])
#creiamo un'area di testo per l'input dell'utente
testo = st.text_area(traduzioni[lingua_interfaccia]["etichetta"], height=200)
files = st.sidebar.file_uploader(traduzioni[lingua_interfaccia]["carica"], accept_multiple_files=True,type=["pdf","txt"]) #creiamo un'area per caricare un file PDF
testo_area = GoogleTranslator(source=detect(testo), target="en").translate(testo) if testo.strip() else ""
testo_completo = testo_area
if files:
    for file in files:
        if file.type == "application/pdf": #se il file è un PDF, estraiamo il testo con pdfplumber
            with pdfplumber.open(file) as pdf:
                testo_file = "\n".join(page.extract_text() for page in pdf.pages)
                #la funzione join() unisce le stringhe estratte da ogni pagina del PDF in un unico testo, separando le pagine con una nuova linea (\n)
                #page.extract_text() estrae il testo da ogni pagina del PDF e lo restituisce come stringa.
        elif file.type == "text/plain": #se il file è un file di testo, leggiamo il contenuto
            testo_file = file.read().decode("utf-8") #decodifichiamo il contenuto del file di testo in formato UTF-8
        testo_file_tradotto = GoogleTranslator(source=detect(testo_file), target="en").translate(testo_file) #traduciamo il testo estratto dal file in inglese, se necessario
        testo_completo += "\n" + testo_file_tradotto #aggiungiamo il testo estratto dal file al testo inserito dall'utente
#creiamo un pulsante per avviare l'analisi
bottoneAnalisi = st.button(traduzioni[lingua_interfaccia]["pulsante"])
if not testo_completo.strip():
    st.session_state.pop("risultati", None)
if bottoneAnalisi:
    if testo_completo.strip():
        with st.spinner(traduzioni[lingua_interfaccia]["spinner"]):
            risultati = classifier(testo_completo, top_k=None, truncation=True, max_length=512)
            st.session_state["risultati"] = risultati
    else:
        st.warning(traduzioni[lingua_interfaccia]["warning"])

if "risultati" in st.session_state: 
    risultati = st.session_state["risultati"]
    st.write(traduzioni[lingua_interfaccia]["risultati"])
    for emozione in risultati:
        st.progress(emozione['score'], text=emoji[lingua_interfaccia][emozione['label']])
    numeroStelle = stelle[risultati[0]['label']]
    st.write(f"{traduzioni[lingua_interfaccia]['valutazione']} {'⭐' * numeroStelle}")
    df = pd.DataFrame(risultati)
    st.sidebar.download_button(
        label=traduzioni[lingua_interfaccia]["esporta"],
        data=df.to_csv(index=False),
        file_name="risultati.csv",
        mime="text/csv"
    )