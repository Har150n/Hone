$(document).ready(function () {
    $('.emotion-button').click(function (event) {
        event.preventDefault();
        var emotion = $(this).text();
        var userId = $(this).data('userid');
        var level = $(this).data('level')
        $.ajax({
            url: '/quiz/' + userId + '/' + level,
            type: 'POST',
            data: {emotion: emotion},
            success: function (response) {
                // Update the content of #response-container with the response HTML
                if (response.completion == 'Complete') {
                    window.location.replace(response.redirect);
                } else if (response.completion == 'Incomplete') {
                    var imageName = response.imageName;
                    var imagePath = '/static/faces/' + imageName;
                    $("img").attr('src', imagePath)
                    $("#scoreValue").text(response.score);
                } else {
                    console.log('Wrong Answer')
                }


            },
            error: function (error) {
                // Handle any errors here, if needed
                console.log(error);
            }
        });
    });


});
