<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
  // Get the form data
  $name = $_POST["name"];
  $email = $_POST["email"];
  $message = $_POST["message"];

  // Email configuration
  $to = "recipient@example.com";  // Replace with the recipient's email address
  $subject = "New contact form submission";
  $body = "Name: $name\nEmail: $email\nMessage: $message";
  $headers = "From: $email";

  // Send the email
  if (mail($to, $subject, $body, $headers)) {
    // Email sent successfully
    header("Location: https://example.com/redirect-page");
    exit();
  } else {
    // Email sending failed
    echo "Failed to send the email.";
  }
}
?>