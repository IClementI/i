<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $subject = $_POST["subject"];
  $message = $_POST["message"];
  
  $to = "destinataire@example.com"; // Adresse e-mail de destination
  $headers = "From: expéditeur@example.com"; // Adresse e-mail de l'expéditeur
  
  // Envoyer l'e-mail
  mail($to, $subject, $message, $headers);
}
?>

