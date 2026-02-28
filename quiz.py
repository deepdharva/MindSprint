from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "Python is a ?",
        "options": ["Snake", "Programming Language", "Car", "Game"],
        "answer": "Programming Language"
    },
    {
        "question": "Symbol used for comment in Python?",
        "options": ["#", "//", "/* */", "--"],
        "answer": "#"
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for i in range(len(questions)):
            user_answer = request.form.get(f"q{i}")
            if user_answer == questions[i]["answer"]:
                score += 1
        return render_template("result.html", score=score)

    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)