<?php
header('Content-Type: text/html; charset=UTF-8');

include 'src/Afip.php';
$afip = new Afip(array(
    'CUIT' => 30710051859,
    'production' => true
));

function armar_cuit($cuit)
{
    $cuit1 = substr($cuit, 0, 2);
    $cuit2 = substr($cuit, 2, 8);
    $cuit3 = substr($cuit, 10, 1);
    $resultado = $cuit1 . "-" . $cuit2 . "-" . $cuit3;
    return $resultado;
}

$return = array();
$return_arr = array();
$data = $afip->RegisterScopeFive->GetTaxpayerDetails($_POST['cuit']);
$cuit = armar_cuit($_POST['cuit']);


if (!isset($data->errorConstancia)):

    if ($data
        ->datosGenerales->tipoPersona == 'JURIDICA'):
        $return['RazonSocial'] = $data
            ->datosGenerales->razonSocial;
    else:
        $return['RazonSocial'] = $data
            ->datosGenerales->apellido . " " . $data
            ->datosGenerales->nombre;
    endif;

    $return['CodigoPostal'] = $data
        ->datosGenerales
        ->domicilioFiscal->codPostal;
    $return['Provincia'] = $data
        ->datosGenerales
        ->domicilioFiscal->descripcionProvincia;
    $return['TipoDomicilio'] = $data
        ->datosGenerales
        ->domicilioFiscal->tipoDomicilio;
    $return['Domicilio'] = $data
        ->datosGenerales
        ->domicilioFiscal->direccion;
    $return['Domicilio'] = mb_convert_encoding($return['Domicilio'], "UTF-8", "HTML-ENTITIES");

    if (isset($data
        ->datosGenerales
        ->domicilioFiscal
        ->localidad)):
        $return['Localidad'] = $data
            ->datosGenerales
            ->domicilioFiscal->localidad;
        $return['Localidad'] = mb_convert_encoding($return['Localidad'], "UTF-8", "HTML-ENTITIES");
    endif;

    $return['TipoDNI'] = "80";

    if (isset($data->datosMonotributo)):
        $return['CondicionIVA'] = 'MONOTRIBUSTISTA ' . $data
            ->datosMonotributo
            ->categoriaMonotributo->descripcionCategoria;
        $return['Factura'] = "B";

    elseif (isset($data
        ->datosRegimenGeneral
        ->impuesto)):
        if (is_array($data
            ->datosRegimenGeneral
            ->impuesto) == true):
            if ($data
                ->datosRegimenGeneral
                ->impuesto[1]->descripcionImpuesto == "IVA" || $data
                ->datosRegimenGeneral
                ->impuesto[0]->descripcionImpuesto == "IVA" || $data
                ->datosRegimenGeneral
                ->impuesto[2]->descripcionImpuesto == "IVA"):
                $return['CondicionIVA'] = 'RESPONSABLE INSCRIPTO';
                $return['Factura'] = "A";
            elseif ($data
                ->datosRegimenGeneral
                ->impuesto[1]->descripcionImpuesto == "IVA EXENTO"):
                $return['CondicionIVA'] = 'IVA EXENTO';
                $return['Factura'] = "B";
            else:
                $return['CondicionIVA'] = 'OTROS';
                $return['Factura'] = "B";
            endif;
        elseif ($data
            ->datosRegimenGeneral->impuesto == "IVA"):
            $return['CondicionIVA'] = 'RESPONSABLE INSCRIPTO';
            $return['Factura'] = "A";
        else:
            $return['CondicionIVA'] = 'CONSUMIDOR FINAL';
            $return['Factura'] = "B";
        endif;

    else:
        $return['CondicionIVA'] = 'CONSUMIDOR FINAL';
        $return['Factura'] = "B";
    endif;

    $return['DNI'] = 'CUIT';

    $return_arr[] = $return;

else:

    if (isset($data
        ->errorConstancia
        ->apellido)):
        $return['TipoDNI'] = "86";
        $return['Factura'] = "B";
        $return['CondicionIVA'] = 'CONSUMIDOR FINAL';
        $return['DNI'] = 'CUIL';
        if (isset($data
            ->errorConstancia
            ->nombre)):
            $return['RazonSocial'] = $data
                ->errorConstancia->apellido . " " . $data
                ->errorConstancia->nombre;
        else:
            $return['RazonSocial'] = $data
                ->errorConstancia->apellido;
        endif;
        $error = $data
            ->errorConstancia->error;

        if (is_array($error) == true):
            $max = count($error);

            for ($i = 0;$i < $max;$i++):
                $errores = $errores . " " . $error[$i];
            endfor;
        else:
            $errores = $error;
        endif;

        $return['error'] = mb_convert_encoding($errores, "UTF-8", "HTML-ENTITIES");

    else:

        $error = $data
            ->errorConstancia->error;

        if (is_array($error) == true):
            $max = count($error);

            for ($i = 0;$i < $max;$i++):
                $errores = $errores . " " . $error[$i];
            endfor;
        else:
            $errores = $error;
        endif;

        $return['error'] = mb_convert_encoding($errores, "UTF-8", "HTML-ENTITIES");
    endif;

    $return_arr[] = $return;
endif;

echo json_encode($return_arr);
?>
