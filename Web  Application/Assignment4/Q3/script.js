let historyArray = [];   // Array to store history

function calculate(){

    let n1 = Number(document.getElementById("num1").value);
    let n2 = Number(document.getElementById("num2").value);
    let op = document.getElementById("operator").value;

    let result;

    // Perform operations
    if(op === "+") result = n1 + n2;
    else if(op === "-") result = n1 - n2;
    else if(op === "*") result = n1 * n2;
    else if(op === "/") result = n2 !== 0 ? n1 / n2 : "Cannot divide by 0";

    document.getElementById("result").innerText =
        "Result: " + result;

    let record = `${n1} ${op} ${n2} = ${result}`;

    // Store in array
    historyArray.unshift(record);

    // Keep only last 5 calculations
    if(historyArray.length > 5){
        historyArray.pop();
    }

    updateHistory();
}

// Update history dynamically using DOM
function updateHistory(){

    let historyList = document.getElementById("history");
    historyList.innerHTML = "";

    historyArray.forEach(item => {
        let li = document.createElement("li");
        li.innerText = item;
        historyList.appendChild(li);
    });
}
