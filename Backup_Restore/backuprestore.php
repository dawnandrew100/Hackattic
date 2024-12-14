<?php
function test() {
    echo "This is a test to make sure PHP is downloaded properly and works";
}

test();

$url = "https://sampleapis.com/";
$curl = curl_init($url);
if($curl) {
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, True);
    $response = curl_exec($curl);
    curl_close($curl);
    echo $response;
}
else {
    echo "Could not run";
}
if(curl_exec($curl) === false)
{
    echo 'Curl error: ' . curl_error($curl);
}
else
{
    echo 'Operation completed without any errors, you have the response';
}
?>
