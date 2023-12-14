var fchmodal = document.getElementById("fchmyModal");
        
// Get the button that opens the modal
var fchbtn = document.getElementById("fchmyBtn");

// Get the <span> element that closes the modal
var fchspan = document.getElementsByClassName("fchclose")[0];

// When the user clicks the button, open the modal 
fchbtn.onclick = function() {
  fchmodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
fchspan.onclick = function() {
  fchmodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == fchmodal) {
    fchmodal.style.display = "none";
  }
}