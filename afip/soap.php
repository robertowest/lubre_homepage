#!/usr/bin/php
<?php
header('Content-Type: text/html; charset=UTF-8');
include '/var/www/html/afip/src/Afip.php';

$afip = new Afip(array('CUIT' => '30710051859', 'production' => true));
// $taxpayer_details = $afip->RegisterScopeFive->GetTaxpayerDetails(20111111111)
$server_status = $afip->RegisterScopeFive->GetServerStatus();

echo 'Este es el estado del servidor:';
echo '<pre>';
print_r($server_status);
echo '</pre>';

?>