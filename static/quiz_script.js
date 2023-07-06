$(document).ready(function () {
    $('.answer-box').click(function (event) {
        event.preventDefault();
        var emotion = $(this).text();
        var userId = $(this).data('userid');
        var level = $(this).data('level')
        $.ajax({
            url: '/quiz/' + userId + '/' + level,
            type: 'POST',
            data: {emotion: emotion},
            success: function (response) {
                let correctSound = new Audio('/static/plop.wav');
                let wrongSound = new Audio('/static/error.wav');
                let completionSound = new Audio('/static/completion.wav');
                // Update the content of #response-container with the response HTML
                if (response.completion == 'Complete') {
                    completionSound.play()
                    setTimeout(function () {
                        window.location.replace(response.redirect);

                    }, 750);

                } else if (response.completion == 'Incomplete') {
                    var imageName = response.imageName;
                    var imagePath = '/static/faces/' + imageName;
                    $("#faceImage").attr('src', imagePath)
                    $("#scoreValue").text(response.score);
                    var SCORE_TO_LEVEL_UP = 10
                    $('.w3-green').css('width', ((response.score / SCORE_TO_LEVEL_UP) * 100) + '%');
                    // play sound
                    correctSound.play()
                } else {
                    wrongSound.play()
                }


            },
            error: function (error) {
                // Handle any errors here, if needed
                console.log(error);
            }
        });
    });


});
