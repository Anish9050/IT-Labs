let textarea = document.getElementById("textInput");
let counter = document.getElementById("count");

const maxLimit = 200;

// input event for real-time checking
textarea.addEventListener("input", function(){

    let currentLength = textarea.value.length;

    let remaining = maxLimit - currentLength;

    counter.innerText = remaining;

    // Prevent typing after limit
    if(currentLength >= maxLimit){
        textarea.value =
            textarea.value.substring(0, maxLimit);
    }
});