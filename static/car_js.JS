
// let slideIndex = 0;
// showSlides();

// function showSlides() {
//   let i;
//   let slides = document.getElementsByClassName("mySlides");
//   let dots = document.getElementsByClassName("dot");
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";  
//   }
//   slideIndex++;
//   if (slideIndex > slides.length) {slideIndex = 1}    
//   for (i = 0; i < dots.length; i++) {
//     dots[i].className = dots[i].className.replace(" active", "");
//   }
//   slides[slideIndex-1].style.display = "block";  
//   dots[slideIndex-1].className += " active";
//   setTimeout(showSlides, 2000); 
// }

// var unreadNotificationsCount = 3;
// function updateNotificationCount() {
//   $('.notification-count').text(unreadNotificationsCount);
// }

function getCSRFToken() {
  var cookies = document.cookie.split(';');
  for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.startsWith('csrftoken=')) {
          return cookie.substring('csrftoken='.length, cookie.length);
      }
  }
  return '';
}

$(document).ready(function() { 

  function updateNotificationCount() {
    // Fetch the unread notifications count from the server and update the count
    $.get("slots/get_unread_notification_count", function(data) {
        var unreadNotificationsCount = data.count;
        $('.notification-count').text(unreadNotificationsCount);
    });
  }
 updateNotificationCount();
    $("#notification-trigger").click(function(e) {
        e.preventDefault();
        $.get("slots/list_notifications", function(response) {
          // Update the dropdown content with the received data
          var notification_data = response.notifications;
          //console.log("hs ");
          var notificationList = $(".notification-list");
          notificationList.empty();

          for (var i = 0; i < notification_data.length; i++) {
            var notificationMessage = notification_data[i].message;
            var notificationItem = $("<li class='noti' >").text(notificationMessage);
            notificationList.append(notificationItem);
        }
         $("#notification-menu").toggle();

         markAllNotificationsAsRead();

         updateNotificationCount();
          //console.log("uhgc gag a ");
        });
      });

      $("#clear-notifications-btn").click(function(e) {

        e.preventDefault();
        // Add logic here to clear notifications (e.g., make an AJAX request)
        var csrfToken = getCSRFToken();
        $.ajax({
            url: "slots/clear_all_notifications",
            type: "POST",
            headers: { "X-CSRFToken": csrfToken },
            success: function() {
                // After clearing notifications, update the notification count
                updateNotificationCount();
                //$("#notification-menu").hide();
            }
        });
    });

    function markAllNotificationsAsRead() {
      var csrfToken = getCSRFToken();
      $.ajax({
          url: "slots/mark_notification_as_read",
          type: "POST",
          headers: { "X-CSRFToken": csrfToken },
          success: function() {
              // After marking all notifications as read, update the notification count
              updateNotificationCount();
          }
      });
  }

      function hideDropdown() {
          
          $(".dropdown-menu").hide();
          $("#notification-menu").hide();
      }
     
    //   $("#profile-icon").click(function(event) {
    //       event.stopPropagation();          
    //       $(".dropdown-menu").toggle();
    //   });
      
    //   $(document).click(function() {
    //       hideDropdown();
    //   });
    
      
    //   $(window).scroll(function() {
    //       hideDropdown();
    //   });


    $("#profile-icon").click(function(event) {
        event.stopPropagation();
        $("#profile-dropdown").toggle();
    });

    $(document).click(function(event) {
        if (!$(event.target).is("#profile-icon")) {
            hideDropdown();
        }
    });

    $(window).scroll(function() {
        hideDropdown();
    });

 
});  
    
    
    
    
document.addEventListener("DOMContentLoaded", function () {
        const loginTrigger = document.getElementById("login-trigger");
        const loginDropdown = document.getElementById("login-dropdown");
    
     
    
        loginTrigger.addEventListener("click", function (event) {
            event.preventDefault();
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
    
    //     document.getElementById('scrolltofooter').addEventListener('click', function() {
    //     document.querySelector('.foot').scrollIntoView({ behavior: 'smooth' });
    // });
    
  });

  