// Add items dynamically
function addItem(){

    let input = document.getElementById("itemInput");
    let value = input.value.trim();

    if(value === ""){
        alert("Enter item");
        return;
    }

    let li = document.createElement("li");
    li.innerText = value;

    document.getElementById("itemList")
            .appendChild(li);

    input.value = "";
}


// Live filtering using onkeyup + filter()
function filterItems(){

    let searchText =
        document.getElementById("searchBox")
        .value.toLowerCase();

    let items =
        document.querySelectorAll("#itemList li");

    Array.from(items).filter(item => {

        let text = item.innerText.toLowerCase();

        if(text.includes(searchText))
            item.style.display = "block";   // show
        else
            item.style.display = "none";    // hide
    });
}