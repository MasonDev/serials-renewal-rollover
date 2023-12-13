// static/script.js
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    const loadingSpinner = document.getElementById('loading-spinner');
    const successTick = document.getElementById('success-tick');

    form.addEventListener('submit', function(event) {
        // Show the loading spinner when the form is submitted
        loadingSpinner.style.display = 'inline-block';

        // Prevent the default form submission
        event.preventDefault();

        // Create a FormData object and append the file input value
        const formData = new FormData(form);
        const fileInput = form.querySelector('input[type="file"]');
        formData.append('file', fileInput.files[0]);

        // Make a Fetch API request to the server
        fetch('/process', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.blob();
        })
        .then(blob => {
            // Create a Blob URL and initiate the download
            const blobUrl = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = blobUrl;
            a.download = 'output.xlsx';
            a.click();

            // Hide the loading spinner
            loadingSpinner.style.display = 'none';

            // Show the success tick
            successTick.style.display = 'flex';

            // Trigger additional events or actions as needed
            console.log('File download completed!');
        })
        .catch(error => {
            // Handle errors if needed
            console.error('Error in file download:', error);
        });
    });
});
