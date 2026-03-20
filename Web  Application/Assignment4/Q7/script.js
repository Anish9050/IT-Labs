// Check session when page loads
window.onload = function(){

    let storedUser = localStorage.getItem("username");

    if(storedUser){
        showWelcome(storedUser);
    }
};

// Login function
function login(){

    let user =
        document.getElementById("username").value.trim();

    if(user === ""){
        alert("Enter username");
        return;
    }

    // Save username
    localStorage.setItem("username", user);

    showWelcome(user);
}

// Show welcome message
function showWelcome(user){

    document.getElementById("loginSection")
        .style.display = "none";

    document.getElementById("welcomeSection")
        .style.display = "block";

    document.getElementById("welcomeMsg")
        .innerText = "Welcome back, " + user;
}

// Logout function
function logout(){

    // Clear storage
    localStorage.removeItem("username");

    location.reload();
}