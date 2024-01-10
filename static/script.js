document.addEventListener('DOMContentLoaded', function() {
    const videoElement = document.getElementById('videoElement');
    const loginBtn = document.getElementById('loginBtn');
    let stream;

    // Access the webcam and stream the video to the videoElement
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(mediaStream) {
        stream = mediaStream;
        videoElement.srcObject = mediaStream;
        videoElement.onloadedmetadata = function(e) {
            videoElement.play();
        };
    })
    .catch(function(err) {
        console.log("An error occurred: " + err);
    });

    loginBtn.addEventListener('click', function() {
        // Stop the video stream
        stream.getTracks().forEach(function(track) {
            track.stop();
        });

        // Redirect to the happy page
        window.location.href = "/happy";
    });
});
