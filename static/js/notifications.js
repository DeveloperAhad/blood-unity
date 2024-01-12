$(document).ready(function () {
    $("#notificationDropdown").click(function () {
        $(".notification-list").toggle();
    });

    // Close the dropdown when clicking outside of it
    $(document).on("click", function (event) {
        if (!$(event.target).closest(".notification-dropdown").length) {
            $(".notification-list").hide();
        }
    });


    var url = 'http://localhost:8002/notifications/';
    csrf_token = $('input[name=csrfmiddlewaretoken]').val()

    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrf_token
        }
    });

    var notificationWrapper = $('.notifications-wrapper');

// Make the AJAX request
    $.ajax({
        type: 'GET', // Change this to the desired HTTP method (GET, POST, etc.)
        url: url,
        success: function (response) {
            console.log();
            // Handle the successful response here
            response?.notifications.map((notification) => {
                notificationWrapper.prepend(`
                       <a class="content" href="#">
                                <div class="notification-item">
                                    <h4 class="item-title">${notification.title} · ${notification.date}</h4>
                                    <p class="item-info">${notification.content}</p>
                                </div>

                            </a>
                `)
            })
        },
        error: function (error) {
            console.log(error);
            // Handle the error here
        }
    });

    var socket = new WebSocket('ws://localhost:8002/ws/notifications/')

    socket.onmessage = function (e) {
        var data = JSON.parse(e.data);
        console.log(data)
        if (data.type == "send_notification") {
            notificationWrapper.prepend(`
                       <a class="content" href="#">
                                <div class="notification-item">
                                    <h4 class="item-title">${data.title} · ${data.date}</h4>
                                    <p class="item-info">${data.content}</p>
                                </div>

                            </a>
                `)
        }
    }


});




