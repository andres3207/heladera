<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head>
 	<title>Sistema de Monitoreo de Humedad y Temperatura</title>
 	<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1" >
   	<link href="<?php echo base_url();?>css/general.css" media="screen,print" rel="stylesheet" type="text/css" />




</head>
<script type="text/javascript">
jQuery(document).ready(function() {
});
</script>
<style type="text/css">
</style>

<?php
$cant_reg=count($datos["datos"]);
//echo $cant_reg;
//exit();
?>

<div class="container">
<div class="form-horizontal">
<h2>Datos:</h2>
<form action='registros' method="POST">
<h3>Filtrar por fecha</h3>
<div class="form-group">
<label class='col-md-2 text-left'><p>Desde:<span>aaaa-mm-dd</span></p></label>
<div class="col-md-2"><p><input type='text' class="form-control" id="desde" name="desde"></input></p></div>
<div class="col-md-1"></div>
<label class='col-md-2'><p>Hasta:<span>aaaa-mm-dd</span></p></label>
<div class="col-md-2"><p><input type='text' class="form-control" id="hasta" name="hasta"></input></p></div>
<div class="col-md-1"><input type="submit" name="mostrar" class="btn btn-info" value="Mostrar"></div>
<div class="col-md-1"><input type="submit" name="mostrar" class="btn btn-info" value="Descargar"></div>
</div>
</form>
<div class="form-group">
<div class="col-md-12"><p>

<table class='table'>
	<tr>
	<td><p>Temperatura</p></td>
	<td><p>Humedad</p></td>
	<td><p>Fecha</p></td>
	</tr>
	<?php
	for ($i=0; $i <$cant_reg ; $i++) { 
		echo "<tr>";
		if ($datos["datos"][$i]["temperatura"]<=$datos["limites"]["t_min"]) {
			echo "<td class='info'><p>".$datos["datos"][$i]["temperatura"]."</p></td>";
		}elseif ($datos["datos"][$i]["temperatura"]<=$datos["limites"]["t_max"]) {
			echo "<td class='success'><p>".$datos["datos"][$i]["temperatura"]."</p></td>";
		}else{
			echo "<td class='danger'><p>".$datos["datos"][$i]["temperatura"]."</p></td>";
		}
		if ($datos["datos"][$i]["humedad"]<=$datos["limites"]["h_min"]) {
			echo "<td class='info'><p>".$datos["datos"][$i]["humedad"]."</p></td>";
		}elseif ($datos["datos"][$i]["humedad"]<=$datos["limites"]["h_max"]) {
			echo "<td class='success'><p>".$datos["datos"][$i]["humedad"]."</p></td>";
		}else{
			echo "<td class='danger'><p>".$datos["datos"][$i]["humedad"]."</p></td>";
		}
		//echo "<td>".$datos["datos"][$i]["temperatura"]."</td>";
		//echo "<td>".$datos["datos"][$i]["humedad"]."</td>";
		echo "<td><p>".$datos["datos"][$i]["cuando"]."</p></td>";
		echo "</tr>";
	}
	
	?>
</table>

<!--
<?php
for ($i=0; $i < $cant_reg; $i++) { 
		echo "<input type='text' id='id-".$i."' name='id-".$i."' value='".$datos["datos"][$i]["id"]."' hidden>";
		echo "<input type='text' id='temp-".$i."' name='temp-".$i."' value='".$datos["datos"][$i]["temperatura"]."' hidden>";
		echo "<input type='text' id='hum-".$i."' name='hum-".$i."' value='".$datos["datos"][$i]["humedad"]."' hidden>";
		echo "<input type='text' id='fecha-".$i."' name='fecha-".$i."' value='".$datos["datos"][$i]["cuando"]."' hidden>";
	}
	?> -->
</p></div>
</div>


</div>
</div>