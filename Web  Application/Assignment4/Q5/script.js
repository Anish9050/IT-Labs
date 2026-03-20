let timer;

// Start countdown
function startTimer(){

    let time =
        Number(document.getElementById("seconds").value);

    if(time <= 0){
        alert("Enter valid seconds");
        return;
    }

    document.getElementById("display").innerText = time;

    // setInterval for countdown
    timer = setInterval(function(){

        time--;

        document.getElementById("display").innerText = time;

        if(time <= 0){
            clearInterval(timer);
            document.getElementById("display")
                .innerText = "Time Over";
        }

    },1000);
}