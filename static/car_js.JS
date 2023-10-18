
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
      $("#notification-trigger").click(function(e) {

        e.preventDefault();

        $.get("slots/list_notifications", function(response) {

          // Update the dropdown content with the received data

          var notification_data = response.notifications;

          //console.log("hs ");

          var notificationMenu = $("#notification-menu");

          notificationMenu.empty();

 

          for (var i = 0; i < notification_data.length; i++) {

            var notificationMessage = notification_data[i].message;

            var notificationItem = $("<li class='notifi'>").text(notificationMessage);

            notificationMenu.append(notificationItem);

        }


          //$("#notification-menu").html(data);

          // Show the dropdown

         // console.log(data);

         notificationMenu.toggle();

          //console.log("uhgc gag a ");

        });

      });
      
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

  // Initialize the carousel when the document is ready
  $(document).ready(function () {
    $('#imageSlideshow').carousel();
  });

  // Move to the next slide
  function nextSlide() {
    $('#imageSlideshow').carousel('next');
  }

  // Move to the previous slide
  function prevSlide() {
    $('#imageSlideshow').carousel('prev');
  }

  // Auto-slide the carousel every 2 seconds (optional)
  $('#imageSlideshow').carousel({
    interval: 2000, // Auto-slide interval in milliseconds (2 seconds)
  });





