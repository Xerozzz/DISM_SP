//Contact Form
function validateContactsForm(){
    var email = document.forms["form"]["email_contact"];    
    
    if (email.value == email.value.indexOf('@') == -1 || email.value.indexOf('.') == -1)
    { 
        window.alert("Please enter a valid email."); 
        email.focus(); 
        return false; 
    } 
   
    else {
        return true
    }
}

//Donation Form
function validateDonateForm(){
    var email = document.forms["form_donate"]["email_donate"];  //For email (Danation form) 
    var ccnum = document.forms["form_donate"]["cc_num"];   //For CC number validation
    var expyear = document.forms["form_donate"]["exp_year"]; //For expiry year
    var donateAmount = document.forms["form_donate"]["donate_amount"]    

    if (email.value == email.value.indexOf('@') == -1 || email.value.indexOf('.') == -1)
    { 
        window.alert("Please enter a valid email."); 
        email.focus(); 
        return false; 
    }

    var cardno = /[0-9\-]{19}/;
    if(ccnum.value != ccnum.value.match(cardno) || ccnum.value == "")
    { 
        window.alert("Please enter a valid credit card number."); 
        ccnum.focus(); 
        return false; 
    }

    if (parseInt(expyear.value) < 2019 || isNaN(expyear.value) == true || expyear.value == "" || (expyear.value).length != 4 ) //Check if expiry year entered is less than 2019, empty or an illegal number
    { 
        alert("Please enter a valid date of expiration for your credit card."); 
        expyear.focus(); 
        return false; 
    }

    if (isNaN(donateAmount.value) == true || donateAmount.value == "")
    {
        alert("Please enter a number");
        donateAmount.focus();
        return false;
    }

    else{
        return true
    }
}