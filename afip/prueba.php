#!/usr/bin/php
<?php
header('Content-Type: text/html; charset=UTF-8');
include '/var/www/html/afip/src/Afip.php';

if ($argc != 2) {
   die("Debe informar el CUIT que desea consultar: prueba.php <CUIT> \n");
}

function armar_cuit($cuit)
{
    $cuit1 = substr($cuit, 0, 2);
    $cuit2 = substr($cuit, 2, 8);
    $cuit3 = substr($cuit, 10, 1);
    $resultado = $cuit1 . "-" . $cuit2 . "-" . $cuit3;
    return $resultado;
}

// print_r($argv); 
$cuit = $argv[1];
print_r( armar_cuit($cuit) );
print_r("\n");

$return = array();
$return_arr = array();
$afip = new Afip(array('CUIT' => '30710051859', 'production' => true));
$data = $afip->RegisterScopeFive->GetTaxpayerDetails($cuit);

print_r("\n");
print_r( $data );

?>
