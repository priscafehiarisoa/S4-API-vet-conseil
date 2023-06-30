setTimeout(function(){
       var successMessages = document.getElementsByClassName('alert-success');
       successMessages[0].style.display = 'none';
       var errorMessages = document.getElementsByClassName('alert-danger')
        errorMessages[0].style.display = 'none';
    }, 1000);