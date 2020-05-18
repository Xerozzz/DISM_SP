function validateForm(){
    var email = document.forms["form"]["email"];    
    var ccnum = document.forms["form"]["ccnum"];  
    var expyear = document.forms["form"]["expyear"];
    var cvv = document.forms["form"]["cvv"];      
   
    if (email.value == email.value.indexOf('@') == -1 || email.value.indexOf('.') == -1)
    { 
        window.alert("Please enter your email."); 
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

    if (parseInt(expyear.value) < 2019 || isNaN(expyear.value) == true|| expyear.value == "")
    { 
        alert("Please enter a valid date of expiration for your credit card."); 
        expyear.focus(); 
        return false; 
    }

    var cardnumber = /[0-9]{3}/;
    if (cvv.value != cvv.value.match(cardnumber)){ 
        window.alert("Please enter a valid cvv."); 
        cvv.focus(); 
        return false; 
    }       

    else {
        return true
    }
}