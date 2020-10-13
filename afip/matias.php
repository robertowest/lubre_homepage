<?php
$archivo = "conf.ini";
$contenido = parse_ini_file($archivo, true);

header('Content-Type: text/html; charset=UTF-8');
header("Access-Control-Allow-Origin: *");
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>AFIP</title>

        <link href="images/favicon-32x32.png" rel="icon" type="image/x-icon"/>
        <link href="images/favicon-32x32.png" rel="shortcut icon" type="image/x-icon"/>
        <link href="images/favicon-32x32.png" rel="shortcut icon" type="image/vnd.microsoft.icon"/>
        <link href="images/favicon-32x32.png" rel="icon" type="image/vnd.microsoft.icon"/>

		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" type="text/css" />
        <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/themes/base/minified/jquery-ui.min.css" type="text/css" />

        <!--
        <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
        <script type="text/javascript" src="http://code.jquery.com/ui/1.10.1/jquery-ui.min.js"></script>
        <script src="js/script.js"></script>
		<script type="text/javascript" src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        -->
        <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
        <script type="text/javascript" src="http://code.jquery.com/ui/1.10.1/jquery-ui.min.js"></script>
		<script type="text/javascript" src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

    </head>

    <body class="bg-light">
        <div class="container">
            <div class="py-2">
                <h5>CONSULTAR DATOS
                  <?php
                  if($contenido['Afip']['produccion'] == false){
                    echo '- HOMOLOGACION';
                  }elseif($contenido['Afip']['produccion'] == true){
                    //echo '- PRODUCCION';
                  }
                   ?>
                </h5>
                <form id="PedidoNuevo" name="PedidoNuevo" method="post" action="matias.php">
                    <div class="card">
                        <div class="card-body">

                            <div class="form-row">
                                <div class="form-group col-md-2">
                                    <label for="cuit"><small>CUIT:</small></label>
                                    <!--
                                    <input type="text" id="cuit" class="form-control form-control-sm" name="cuit" onkeyup="buscar_cliente(this.value);" required maxlength="11"/>
                                    -->
                                    <input type="text" id="cuit" class="form-control form-control-sm" name="cuit" onkeypress="buscar_cliente(event);" required maxlength="11"/>
                                </div>
                                <div class="form-group col-md-5">
                                    <label for="razonsocial"><small>Razon Social:</small></label>
                                    <input type="text" id="razonsocial" name="razonsocial" class="form-control form-control-sm" readonly/>
                                </div>
                            </div>
                            <div class="form-row">
                                <div class="form-group col-md-5">
                                    <label for="domicilio_fiscal"><small>Domicilio:</small></label>
                                    <input type="text" id="domicilio_fiscal" name="domicilio_fiscal" class="form-control form-control-sm" readonly/>
                                </div>
                                <div class="form-group col-md-2">
                                    <label for="codigo_postal"><small>CODIGO POSTAL:</small></label>
                                    <input type="text" id="codigo_postal" class="form-control form-control-sm" name="codigo_postal" readonly/>
                                </div>

                            </div>
                            <div class="form-row">
                            <div class="form-group col-md-5">
                                    <label for="provincia"><small>PROVINCIA:</small></label>
                                    <input type="text" id="provincia" name="provincia" class="form-control form-control-sm" readonly/>
                                </div>
                                <div class="form-group col-md-5">
                                    <label for="localidad"><small>LOCALIDAD:</small></label>
                                    <input type="text" id="localidad" name="localidad" class="form-control form-control-sm" readonly/>
                                </div>
                            </div>
                            <div class="form-row">
                                <div class="form-group col-md-5">
                                    <label for="condicion_iva"><small>Condicion IVA:</small></label>
                                    <input type="text" id="condicion_iva" name="condicion_iva" class="form-control form-control-sm" readonly/>
                                </div>
                                <div class="form-group col-md-2">
                                    <label for="dni"><small>TIPO:</small></label>
                                    <input type="text" id="dni" class="form-control form-control-sm" name="dni" readonly/>
                                </div>
                                <div class="form-group col-md-2">
                                    <label for="tipo_dni"><small>CONDICION:</small></label>
                                    <input type="text" id="tipo_dni" class="form-control form-control-sm" name="tipo_dni" readonly/>
                                </div>
                                <div class="form-group col-md-2">
                                    <label for="letra"><small>LETRA:</small></label>
                                    <input type="text" id="letra" class="form-control form-control-sm" name="letra" readonly/>
                                </div>
                            </div>

                        <p id="error"></p>
                        </div>
                    </div>
                </form>
                
                <div id="cliente_bd">
                </div>
            </div>
        </div>
    </body>

    <script type="text/javascript">
        // http://192.168.1.9/nlp/nueva_factura.php
        // http://192.168.1.9/nlp/buscar_cliente_afip.php

        function buscar_cliente(e) {
            if (e.keyCode === 13 && !e.shiftKey) {
                e.preventDefault();
                var cuit = $("#cuit").val();

                jQuery.ajax({
                    url: 'http://192.168.1.9/nlp/buscar_cliente_afip.php',
                    type: "POST",
                    data: "cuit="+cuit,
                    dataType: "json",
                    success: function(datos) {     
                        // alert(JSON.stringify(datos));                    
                        jQuery("#razonsocial").val(datos[0]['RazonSocial']);
                        jQuery("#domicilio_fiscal").val(datos[0]['Domicilio']);
                        jQuery("#letra").val(datos[0]['Factura']);
                        jQuery("#tipo_dni").val(datos[0]['TipoDNI']);
                        jQuery("#condicion_iva").val(datos[0]['CondicionIVA']);
                        jQuery("#provincia").val(datos[0]['Provincia']);
                        jQuery("#localidad").val(datos[0]['Localidad']);
                        jQuery("#codigo_postal").val(datos[0]['CodigoPostal']);
                        jQuery("#dni").val(datos[0]['DNI']);
                        jQuery("#error").html(datos[0]['error']);
                        
                        // jQuery("#cliente_bd").html(datos[0]);
                        console.log(datos[0]);
                    },
                    error: function(xhr, status, error) {
                        console.log(xhr.responseText);
                        alert('Error en la petición');
                    },
                });
            };
        };
     </script>
</html>
