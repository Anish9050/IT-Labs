let students = [];

// Fetch JSON data
fetch("students.json")
.then(response => response.text())
.then(data => {

    // JSON.parse()
    students = JSON.parse(data);

    displayTable(students);
});


// Display table dynamically
function displayTable(data){

    let tbody = document.getElementById("tableBody");
    tbody.innerHTML = "";

    data.forEach(student => {

        let row = document.createElement("tr");

        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.course}</td>
            <td>${student.marks}</td>
        `;

        tbody.appendChild(row);
    });
}


// Search function
function searchStudent(){

    let keyword =
        document.getElementById("search")
        .value.toLowerCase();

    let filtered = students.filter(student =>
        student.name.toLowerCase().includes(keyword)
    );

    displayTable(filtered);
}