# 🎭 Analisi delle Emozioni con IA

Web-app che analizza le emozioni presenti in un testo (scritto direttamente o caricato da file PDF/TXT), utilizzando un modello di Natural Language Processing pre-addestrato di HuggingFace.

## 📌 Descrizione

L'applicazione permette all'utente di inserire un testo libero oppure di caricare uno o più file (PDF o TXT) e restituisce un'analisi dettagliata delle emozioni rilevate: **gioia, tristezza, rabbia, paura, sorpresa, disgusto, neutralità**.

Se il testo non è in inglese, viene rilevata automaticamente la lingua e tradotto prima dell'analisi, poiché il modello di classificazione lavora su testo in lingua inglese.

## ✨ Funzionalità

- 📝 Analisi di testo inserito manualmente
- 📄 Caricamento multiplo di file PDF e TXT, con estrazione automatica del testo
- 🌍 Interfaccia disponibile in 6 lingue: Italiano, English, Deutsch, Français, Español, Português
- 🌐 Rilevamento automatico della lingua del testo e traduzione in inglese quando necessario
- 📊 Visualizzazione del punteggio per ciascuna emozione rilevata, con barra di progresso ed emoji
- ⭐ Valutazione sintetica dell'esperienza espressa nel testo, su una scala da 1 a 5 stelle
- 📥 Esportazione dei risultati in formato CSV

## 🛠️ Stack tecnologico

- **Python**
- **[Streamlit](https://streamlit.io/)** — interfaccia web
- **[Transformers](https://huggingface.co/docs/transformers)** (HuggingFace) — classificazione delle emozioni, modello [`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)
- **[pdfplumber](https://github.com/jsvine/pdfplumber)** — estrazione del testo dai PDF
- **[deep-translator](https://pypi.org/project/deep-translator/)** — traduzione automatica del testo
- **[langdetect](https://pypi.org/project/langdetect/)** — rilevamento della lingua
- **[pandas](https://pandas.pydata.org/)** — gestione ed esportazione dei risultati

## 🚀 Installazione

Clona il repository:

```bash
git clone https://github.com/piccinalipezzoliluca/analisiEmozioniAI.git
cd analisiEmozioniAI/analizzaEmozioni
```

Installa le dipendenze necessarie:

```bash
pip install streamlit transformers torch pdfplumber deep-translator langdetect pandas
```

## ▶️ Utilizzo

Avvia l'applicazione con:

```bash
python -m streamlit run app.py
```

Si aprirà automaticamente una pagina nel browser. Da qui puoi:

1. Scegliere la lingua dell'interfaccia dal menu a tendina nella sidebar
2. Scrivere un testo nell'area dedicata **oppure** caricare uno o più file PDF/TXT
3. Cliccare su **"Analizza Emozioni"**
4. Visualizzare i punteggi per ogni emozione e la valutazione complessiva
5. (Facoltativo) Esportare i risultati in CSV dalla sidebar

> ⚠️ Nota: il modello analizza fino a 512 token per volta; testi più lunghi vengono troncati automaticamente.

## 📂 Struttura del progetto

```
analizzaEmozioni/
├── app.py          # Interfaccia Streamlit e logica principale
├── config.py        # Traduzioni, emoji e mappatura emozioni → valutazione a stelle
```

## 👤 Autore

Sviluppato da **Luca Piccinali Pezzoli**
