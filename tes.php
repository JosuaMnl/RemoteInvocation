<?php
header('Content-Type: application/json; charset=utf-8');
$hasil = $_GET['a'] + $_GET['b'];

$data = array(
    "status" => 1,
    "data" => array("a" => floatval($_GET["a"])) + floatval($_GET['b']),
    "tulisan" => "Halo World",
);

print json_encode($data);