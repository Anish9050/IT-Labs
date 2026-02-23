let generatedOTP = "";

// Generate OTP using Math.random()
function generateOTP(){

    generatedOTP = Math.floor(100000 + Math.random() * 900000);

    document.getElementById("otpDisplay")
            .innerText = "Generated OTP: " + generatedOTP;

    document.getElementById("message").innerText = "";
}

// Verify OTP
function verifyOTP(){

    let enteredOTP =
        document.getElementById("userOTP").value;

    if(enteredOTP == generatedOTP){
        document.getElementById("message").innerText =
            "✅ Valid OTP";
        document.getElementById("message").style.color="green";
    }
    else{
        document.getElementById("message").innerText =
            "❌ Invalid OTP";
        document.getElementById("message").style.color="red";
    }
}