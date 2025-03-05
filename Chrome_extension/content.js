// Variable to store the previously selected image and audio object
let previouslySelectedImage = null;
let audio = null;


function speak(message, callback) {
    const speech = new SpeechSynthesisUtterance(message);
    speech.rate = 1; // Adjust speech rate if needed
    speech.onend = callback; // Call the callback after speech ends
    window.speechSynthesis.speak(speech);
}

document.addEventListener('click', function (event) {
    let target = event.target;
    
    if (target.tagName.toLowerCase() === 'img') {
        // Add a border and shadow to indicate selection
        target.style.border = '5px solid #FF5733'; // Customize the color and thickness as needed
        target.style.borderRadius = '10px';
        target.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)'; // Add shadow effect

        // Remove the border and shadow from the previously selected image if it exists
        if (previouslySelectedImage && previouslySelectedImage !== target) {
            previouslySelectedImage.style.border = ''; // Remove the border
            previouslySelectedImage.style.boxShadow = ''; // Remove the shadow
        }

        // Update the previously selected image
        previouslySelectedImage = target;

        // Provide verbal confirmation for image selection
        speak("Image selected");

        // Trigger a short vibration pattern for haptic feedback if supported
        if (navigator.vibrate) {
            navigator.vibrate([100, 50, 100]); // Vibration pattern: vibrate-pause-vibrate
        }

        // Extract the 'src' attribute
        let imgSrc = target.src;

        // Send the image source URL to the Flask application
        fetch('https://echolens.onrender.com/get_desc', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image_url: imgSrc })
        })
        .then(response => response.blob()) // Receive audio as a blob
        .then(blob => {
            // Provide verbal confirmation for playing description and wait for it to finish
            speak("Playing description", () => {
                // Create a URL for the audio file and play it
                const audioUrl = URL.createObjectURL(blob);
                audio = new Audio(audioUrl); // Store the audio object for later access

                // Set the playback rate to 1.15x
                audio.playbackRate = 1.15;
                
                // Play the audio
                audio.play();

                // Optional: Revoke the object URL after the audio has played to clean up resources
                audio.onended = () => {
                    URL.revokeObjectURL(audioUrl);
                    speak("Playback stopped"); // Verbal confirmation for playback stop
                };
            });
        })
        .catch(error => console.error('Error:', error));

        event.preventDefault();
    }
}, true);

// Event listener for stopping the audio and removing styles with 'Esc' or 'Space' key
document.addEventListener('keydown', function (event) {
    if (audio && (event.key === 'Escape' || event.key === ' ')) { // ' ' is the space bar
        // Stop the audio playback
        audio.pause();
        audio.currentTime = 0;

        // Provide verbal confirmation for stopping playback
        speak("Playback stopped");

        // Remove the border and shadow from the previously selected image
        if (previouslySelectedImage) {
            previouslySelectedImage.style.border = '';
            previouslySelectedImage.style.boxShadow = '';
            previouslySelectedImage = null; // Reset the previously selected image
        }
    }
});
