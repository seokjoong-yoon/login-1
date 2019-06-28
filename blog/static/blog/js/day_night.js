function dayNightHandler(x){
    if(x.value === 'night'){
        document.querySelector('body').style.backgroundColor='black';
        document.querySelector('body').style.color='white';
        x.value = 'day';
    }
    else{
        document.querySelector('body').style.backgroundColor='white';
        document.querySelector('body').style.color='black';
        x.value = 'night';
    }
}

// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}