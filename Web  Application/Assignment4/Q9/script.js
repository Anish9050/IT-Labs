// Quiz questions using Objects & Array
let quiz = [
{
    question: "Capital of India?",
    options: ["Mumbai","Delhi","Kolkata","Chennai"],
    answer: "Delhi"
},
{
    question: "2 + 2 = ?",
    options: ["3","4","5","6"],
    answer: "4"
},
{
    question: "HTML stands for?",
    options: [
        "Hyper Text Markup Language",
        "High Text Machine Language",
        "Home Tool Markup Language",
        "None"
    ],
    answer: "Hyper Text Markup Language"
}
];

let currentIndex = 0;
let score = 0;
let selectedAnswer = "";

// Load question dynamically
function loadQuestion(){

    let q = quiz[currentIndex];

    document.getElementById("question")
        .innerText = q.question;

    let optionHTML = "";

    q.options.forEach(opt => {
        optionHTML +=
        `<button onclick="selectAnswer('${opt}')">
            ${opt}
         </button><br>`;
    });

    document.getElementById("options").innerHTML =
        optionHTML;
}

// Store selected answer
function selectAnswer(answer){
    selectedAnswer = answer;
}

// Next question
function nextQuestion(){

    if(selectedAnswer === ""){
        alert("Select an answer");
        return;
    }

    if(selectedAnswer === quiz[currentIndex].answer){
        score++;
    }

    selectedAnswer = "";
    currentIndex++;

    if(currentIndex < quiz.length){
        loadQuestion();
    }
    else{
        showResult();
    }
}

// Show final score
function showResult(){

    document.getElementById("question").innerText =
        "Quiz Finished!";

    document.getElementById("options").innerHTML = "";

    document.getElementById("result").innerText =
        "Your Score: " + score + " / " + quiz.length;
}

// Start quiz
loadQuestion();