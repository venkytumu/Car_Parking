
const FirstNameInput = document.querySelector('input[name="first_name"]');
const LastNameInput = document.querySelector('input[name="last_name"]');

const UsernameInput = document.querySelector('input[name="username"]');
const emailInput = document.querySelector('input[name="email"]');

const passwordInput = document.querySelector('input[name="password1"]');

const confirmPasswordInput = document.querySelector('input[name="password2"]');

const signupButton = document.querySelector('input[name="sub"]');

 

// Function to validate the form data

function validateForm() {

    const firstName = FirstNameInput.value.trim();

    const lastName = LastNameInput.value.trim();

    const Username = UsernameInput.value.trim();

    const email = emailInput.value.trim();

    const password = passwordInput.value;

    const confirmPassword = confirmPasswordInput.value;
    const lengthRegex = /^.{4,20}$/;
    const characterSetRegex = /^[a-zA-Z0-9_-]+$/;
    // const reservedWords = ["admin", "root", "guest"]; 

 

    if (firstName === '' || lastName === '' || Username === '' || email === '' || password === '' || confirmPassword === '') {

        alert('Please fill in all fields.');

        return false;

    }


    if (!lengthRegex.test(Username)) {
        alert("Username must be between 4 and 20 characters.");
        return false;
    } 
    
    if (!characterSetRegex.test(Username)) {
        alert("Username contains invalid characters like @, $, +, %, and _.");
        return false;
    } 
    
   //
    
    if (!/^[A-Za-z]/.test(Username)) {
        alert('Username must start with a letter');
        return false;
        
    } 
    
    if (!/[0-9]/.test(Username)) {
        alert('Username must contain atleast one number');
        return false;
    }
    
 
    
    if (password.length < 8){
        alert('Password should have a minimum length of 8 combinational characters');
        return false;
    }
    
    if (!/[A-Z]/.test(password)){
        alert('Password must include at least one uppercase letter.');
        return false;

    }
    
    if (!/[a-z]/.test(password)){
        alert('Password must include at least one lowercase letter.');
        return false; 
        
    }
    
    if (!/[0-9]/.test(password)){
        alert('Password must include at least one number');
        return false;
    } 
    
    if (!/[!@#$%^&*]/.test(password)){
        alert('Password must include at least one special character.');
        return false;
    }
    
    if (password !== confirmPassword) {
        alert('Passwords do not match. Please try again.');
        return false;
    }
    
    if (!email.endsWith("@gmail.com")) {
            // Email does not contain the required domain
        alert('Email address must end with @gmail.com.');
        return false;

    } 

    return true;

}
const registrationForm = document.forms.registration_form;
    registrationForm.onsubmit = validateForm;
// let popup=document.getElementById("popup");

// function openPopup(){
//     popup.classList.add("open-popup");
//     setTimeout(function () {
//         console.log("uvbhvbvbw");
//         closePopup();
//       }, 5000);
//   }
//   function closePopup(){
//     popup.classList.remove("open-popup");
//     window.location.href="login";
//   }

// document.querySelector('form[name="registration_form"]').addEventListener('submit', function (e) {
//     const isFormValid = validateForm(); // Store the result of validateForm in a variable

//     if (!isFormValid) {
//         e.preventDefault(); // Prevent the form from submitting
//     }
    
//     if (isFormValid) { // Check the stored variable for validation
//         // alert(`Hey ${FirstNameInput.value.trim()}, Your Signup is successfull`);
//         openPopup();

//     }
   
// });
// JavaScript code to handle the response and display the popup

  

