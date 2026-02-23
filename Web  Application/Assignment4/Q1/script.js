let studentCount = 0;

function addStudent() {

    let nameInput = document.getElementById("studentName");
    let name = nameInput.value.trim();

    if(name === ""){
        alert("Enter student name");
        return;
    }

    // create li element
    let li = document.createElement("li");

    // student name text
    let text = document.createTextNode(name);
    li.appendChild(text);

    // create remove button
    let removeBtn = document.createElement("button");
    removeBtn.innerText = "Remove";
    removeBtn.className = "remove";

    // remove student
    removeBtn.onclick = function(){
        li.remove();
        studentCount--;
        updateCount();
    };

    // append button to li
    li.appendChild(removeBtn);

    // append li to ul
    document.getElementById("studentList")
            .appendChild(li);

    studentCount++;
    updateCount();

    nameInput.value = "";
}

// update total count
function updateCount(){
    document.getElementById("count").innerText = studentCount;
}