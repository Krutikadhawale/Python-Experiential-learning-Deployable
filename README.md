<<<<<<< HEAD
# English to Hindi Translator

A simple responsive Flask website using `deep-translator` and MyMemory Translator.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the website:

   ```bash
   python app.py
   ```

5. Open http://127.0.0.1:5000 in your browser.

## Deploy on Render

1. Extract this ZIP file.
2. Upload the project to a GitHub repository.
3. In Render, choose **New + → Web Service** and connect the repository.
4. Render can use the included `render.yaml`; if entering settings manually, use:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Click **Deploy Web Service**.

Translation requires an internet connection and the external MyMemory translation service. Free external services may have usage limits or occasional downtime.
=======
# Python-Experiential-learning-Deployable
>>>>>>> be2b532541b6bd2715085a5bd2a7080d0f536d51
