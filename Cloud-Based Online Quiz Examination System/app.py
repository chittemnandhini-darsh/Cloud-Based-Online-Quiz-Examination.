from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Quiz questions
questions = [
    {
        "id": 1,
        "question": "Which language is mainly used for web page structure?",
        "options": ["Python", "HTML", "Java", "C++"],
        "answer": "HTML"
    },
    {
        "id": 2,
        "question": "Which language is used to style web pages?",
        "options": ["CSS", "Python", "SQL", "Java"],
        "answer": "CSS"
    },
    {
        "id": 3,
        "question": "Which language is used to make web pages interactive?",
        "options": ["HTML", "CSS", "JavaScript", "SQL"],
        "answer": "JavaScript"
    },
    {
        "id": 4,
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Computer Processing User"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "id": 5,
        "question": "Which technology is used to create the backend in this project?",
        "options": ["Flask", "Photoshop", "Bootstrap", "Excel"],
        "answer": "Flask"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    score = 0
    total = len(questions)

    for question in questions:
        question_id = str(question["id"])

        if question_id in data:
            if data[question_id] == question["answer"]:
                score += 1

    percentage = (score / total) * 100

    return jsonify({
        "score": score,
        "total": total,
        "percentage": percentage
    })


@app.route("/result")
def result():
    score = request.args.get("score", 0)
    total = request.args.get("total", len(questions))
    percentage = request.args.get("percentage", 0)

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=percentage
    )


if __name__ == "__main__":
    app.run(debug=True)