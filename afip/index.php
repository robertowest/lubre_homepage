<?php
header('Content-Type: text/html; charset=UTF-8');
include 'src/Afip.php';

function armar_cuit($cuit)
{
    $cuit1 = substr($cuit, 0, 2);
    $cuit2 = substr($cuit, 2, 8);
    $cuit3 = substr($cuit, 10, 1);
    $resultado = $cuit1 . "-" . $cuit2 . "-" . $cuit3;
    return $resultado;
}

function mostrar_cuit()
{
    return armar_cuit($_GET['cuit']);
}

function probar_funcionamiento()
{
    $return = array();
    $return_arr = array();
    $afip = new Afip(array('CUIT' => '30710051859', 'production' => true));
    $data = $afip->RegisterScopeFive->GetTaxpayerDetails($_GET['cuit']);
    print_r($data);
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AFIP</title>
</head>
<body>
    <h1>Prueba de AFIP</h1>
    <p>CUIT: <?=mostrar_cuit()?></p>
    <hr>
    <p><?=probar_funcionamiento()?></p>
</body>
</html>