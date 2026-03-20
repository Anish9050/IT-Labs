// Load saved theme after refresh
window.onload = function(){

    let savedTheme = localStorage.getItem("theme");

    if(savedTheme){
        document.body.className = savedTheme;
    }
};


// Toggle theme
function toggleTheme(){

    // Toggle class
    document.body.classList.toggle("dark");
    document.body.classList.toggle("light");

    // Save preference
    if(document.body.classList.contains("dark")){
        localStorage.setItem("theme","dark");
    }
    else{
        localStorage.setItem("theme","light");
    }
}