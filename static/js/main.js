
// Displays the file before uploading
function displayImage(event) {
    let fileInput = event.target;
    let uploadedImage = document.getElementById("uploadedimage");
    let imageLabel = document.getElementById("imagelabel");

    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            uploadedImage.src = e.target.result;
            uploadedImage.style.display = 'block';
            imageLabel.style.display = 'none';
        };
        reader.readAsDataURL(fileInput.files[0]);
    }
}