function validateForm(){

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value;
    let confirmPassword =
        document.getElementById("confirmPassword").value;

    let valid = true;

    // Clear previous errors
    document.getElementById("nameError").innerText="";
    document.getElementById("emailError").innerText="";
    document.getElementById("passError").innerText="";
    document.getElementById("confirmError").innerText="";
    document.getElementById("successMsg").innerText="";

    // Name validation
    if(name === ""){
        document.getElementById("nameError")
            .innerText="Name cannot be empty";
        valid = false;
    }

    // Email validation
    let emailPattern =
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if(!emailPattern.test(email)){
        document.getElementById("emailError")
            .innerText="Invalid Email Format";
        valid = false;
    }

    // Password validation (uppercase + number)
    let passPattern =
        /^(?=.*[A-Z])(?=.*[0-9]).{6,}$/;

    if(!passPattern.test(password)){
        document.getElementById("passError")
            .innerText="Password must contain uppercase & number";
        valid = false;
    }

    // Confirm password
    if(password !== confirmPassword){
        document.getElementById("confirmError")
            .innerText="Passwords do not match";
        valid = false;
    }

    if(valid){
        document.getElementById("successMsg")
            .innerText="✅ Registration Successful";
        document.getElementById("successMsg")
            .className="success";
    }

    return false; // prevent page reload
}