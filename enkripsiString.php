<?php
// Display the original string
// echo "Original String: " . $simple_string;

// Display the encrypted string
// echo "Encrypted String: " . $encryption . "\n";  
header('Content-Type: application/json; charset=utf-8');

// Store a string into the variable which
// need to be Encrypted
$simple_string = $_GET['text'];

// Store the cipher method
$ciphering = "AES-128-CTR";

// Use OpenSSl Encryption method
$iv_length = openssl_cipher_iv_length($ciphering);
$options = 0;

// Non-NULL Initialization Vector for encryption
$encryption_iv = '1234567891011121';

// Store the encryption key
$encryption_key = "GeeksforGeeks";

// Use openssl_encrypt() function to encrypt the data
$encryption = openssl_encrypt($simple_string, $ciphering,
            $encryption_key, $options, $encryption_iv);

$data = array(
    "status" => "success",
    "text-encrypt" => $encryption
);

print json_encode($data);
?>