// Start Quiz
function startQuiz() {

    let name = document.getElementById("studentName").value;

    if (name.trim() === "") {
        alert("Please enter your name.");
        return;
    }

    localStorage.setItem("studentName", name);

    window.location.href = "/quiz";
}


// Timer
let timeLeft = 300;

function startTimer() {

    let timer = document.getElementById("timer");

    if (!timer) {
        return;
    }

    let countdown = setInterval(function () {

        let minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;

        seconds = seconds < 10 ? "0" + seconds : seconds;

        timer.innerHTML = minutes + ":" + seconds;

        timeLeft--;

        if (timeLeft < 0) {

            clearInterval(countdown);

            alert("Time is over!");

            submitQuiz();
        }

    }, 1000);
}


// Submit Quiz
function submitQuiz() {

    let form = document.getElementById("quizForm");

    if (!form) {
        return;
    }

    let formData = new FormData(form);

    let answers = {};

    for (let [key, value] of formData.entries()) {
        answers[key] = value;
    }

    fetch("/submit", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(answers)

    })

    .then(response => response.json())

    .then(data => {

        window.location.href =
            "/result?score=" +
            data.score +
            "&total=" +
            data.total +
            "&percentage=" +
            data.percentage.toFixed(2);

    })

    .catch(error => {

        console.error(error);

        alert("Something went wrong.");

    });
}


// Start timer automatically on quiz page
document.addEventListener("DOMContentLoaded", function () {

    if (document.getElementById("timer")) {
        startTimer();
    }

});