from flask import Flask, render_template, request
from deep_translator import MyMemoryTranslator

app = Flask(__name__)

def translate(sentence):
    return MyMemoryTranslator(source="english", target="hindi").translate(sentence)

@app.route("/", methods=["GET", "POST"])
def home():
    sentence = ""
    translation = ""
    error = ""

    if request.method == "POST":
        sentence = request.form.get("sentence", "").strip()

        if not sentence:
            error = "Please enter an English sentence."
        else:
            try:
                translation = translate(sentence)
            except Exception:
                error = "Translation failed. Please check your internet connection and try again."

    return render_template(
        "index.html",
        sentence=sentence,
        translation=translation,
        error=error
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
