from flask import Flask, render_template, request

app = Flask(__name__)

faq = {
    "fever": "Fever means high body temperature. Rest and drink water.",
    "diabetes": "Diabetes affects blood sugar levels.",
    "headache": "Headache can be caused by stress or dehydration.",
    "emergency": "In emergency, call local emergency services."
}

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"].lower()
        for key in faq:
            if key in question:
                answer = faq[key]
                break
        if answer == "":
            answer = "Please consult a doctor."

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
