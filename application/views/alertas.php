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
$cant_reg=count($datos["alertas"]);
//echo $cant_reg;
//exit();
?>

<div class="container">
<div class="form-horizontal">
<div class="form-group">
<div class="col-md-12"><p>

<table class='table'>
	<tr>
	<td><p>Mensaje</p></td>
	<td><p>Fecha</p></td>
	</tr>
	<?php
	for ($i=0; $i <$cant_reg ; $i++) { 
		echo "<tr>";
		echo "<td><p>".$datos["alertas"][$i]["mensaje"]."</p></td>";
		echo "<td><p>".$datos["alertas"][$i]["cuando"]."</p></td>";
		echo "</tr>";
	}

	
	?>
</table>


</p></div>
</div>


</div>
</div>




