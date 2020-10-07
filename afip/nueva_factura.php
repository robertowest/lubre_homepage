
<?php

session_name('sistema_nlp');
session_start();

if ($_SESSION['usuario'] == '') {
    header("location:logout.php?error=3");
    exit();
}


$archivo = "conf.ini";
$contenido = parse_ini_file($archivo, true);


header('Content-Type: text/html; charset=UTF-8');


?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <?php  flush(); ?>

        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title><?php echo $contenido['Empresa']['razon_social']?> | NLP</title>

<link href="images/favicon-32x32.png" rel="icon" type="image/x-icon"/>
<link href="images/favicon-32x32.png" rel="shortcut icon" type="image/x-icon"/>
<link href="images/favicon-32x32.png" rel="shortcut icon" type="image/vnd.microsoft.icon"/>
<link href="images/favicon-32x32.png" rel="icon" type="image/vnd.microsoft.icon"/>

        <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
        <script type="text/javascript" src="http://code.jquery.com/ui/1.10.1/jquery-ui.min.js"></script>
        <script src="js/script.js"></script>


        <!--<link type="text/css" rel="stylesheet" href="css/estilo.css" />-->

		<link type="text/css" rel="stylesheet" href="css/bootstrap.min.css" />
		<script type="text/javascript" src="js/bootstrap.min.js"></script>

        <!--css ui-->
        <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/themes/base/minified/jquery-ui.min.css" type="text/css" />
    </head>

    <body class="bg-light">

		<?php include("menus/menu.php"); ?>

        <div class="container">


            <div class="py-2">
                <h5>NUEVA FACTURA
                  <?php
                  if($contenido['Afip']['produccion'] == false){
                    echo '- HOMOLOGACION';
                  }elseif($contenido['Afip']['produccion'] == true){
                    //echo '- PRODUCCION';
                  }
                   ?>
                </h5>
                <form id="PedidoNuevo" name="PedidoNuevo" method="post" action="nueva_nlp2.php">

                <div class="card">
					<div class="card-body">

						<div class="form-row">
							<div class="form-group col-md-2">
                                <label for="cuit"><small>CUIT:</small></label>
							  <input type="text" id="cuit" class="form-control form-control-sm" name="cuit" onkeyup="buscar_cliente(this.value);" required maxlength="11"/>
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
        <footer class="my-5 pt-5 text-muted text-center text-small"><?php echo $contenido['Empresa']['razon_social']?></footer>
    </body>
    <script type="text/javascript">
                    

                    function buscar_cliente(cuit){
                       var largo = cuit.length;
                       if(largo == 11){
                        jQuery.ajax({
                            url: 'buscar_cliente_afip.php',
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
                                
                            }
                        });
                       }else{
                            jQuery("#razonsocial").val('');
                            jQuery("#domicilio_fiscal").val('');
                            jQuery("#letra").val('');
                            jQuery("#tipo_dni").val('');
                            jQuery("#condicion_iva").val('');
                            jQuery("#provincia").val('');
                            jQuery("#localidad").val('');
                            jQuery("#codigo_postal").val('');
                            jQuery("#dni").val('');
                            jQuery("#error").empty();
                       }
                    }

     </script>
</html>
