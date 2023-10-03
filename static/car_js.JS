
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); 
}


$(document).ready(function() {
      console.log("Click event listener is active."); 
    
      
      function hideDropdown() {
          console.log("Clicked or scrolled"); 
          $(".dropdown-menu").hide();
      }
    
      
      $(".profile-icon").click(function(event) {
          event.stopPropagation(); 
          console.log("Clicked"); 
          
          $(".dropdown-menu").toggle();
      });
    
      
      $(document).click(function() {
          hideDropdown();
      });
    
      
      $(window).scroll(function() {
          hideDropdown();
      });
  });
    
    
    
    
    
document.addEventListener("DOMContentLoaded", function () {
        const loginTrigger = document.getElementById("login-trigger");
        const loginDropdown = document.getElementById("login-dropdown");
    
     
    
        loginTrigger.addEventListener("click", function (e) {
            e.preventDefault();
            if (loginDropdown.style.display === "block"|| loginDropdown.style.display === "") {
                loginDropdown.style.display = "none";
            } else {
                loginDropdown.style.display = "block";
            }
        });
    
        document.addEventListener("click", function (e) {
        if (e.target !== loginTrigger && e.target !== loginDropdown) {
            loginDropdown.style.display = "none";
            }
        });
    
        window.addEventListener("scroll", function () {
            loginDropdown.style.display = "none";
        });
    
        document.getElementById('scrolltofooter').addEventListener('click', function() {
        document.querySelector('.foot').scrollIntoView({ behavior: 'smooth' });
    });
    
  });