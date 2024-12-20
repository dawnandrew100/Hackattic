<?php
include 'credentials.php';

function curl_get_contents($url)
{
    $ch = curl_init();

    //curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    if(curl_exec($ch) === false)
    {
        throw new Exception('Curl error: '.curl_error($ch), 1);
    }
    $data = curl_exec($ch);
    curl_close($ch);
    return $data;
}

$response = curl_get_contents('https://hackattic.com/challenges/backup_restore/problem?access_token=' . $token);
$decoded_json = json_decode($response, true);

//echo var_dump($decoded_json["dump"]) . "<br>\r\n";
$input = base64_decode($decoded_json["dump"], true);
//echo $input;

$servername = "localhost";
$username = $myusername;
$dbname = "hackattic_db_restore";

try {
  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  echo "Connected successfully";
} catch(PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
}
$conn = null;

?>
