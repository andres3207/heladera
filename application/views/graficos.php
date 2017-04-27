<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head>
 	<title>Sistema de Monitoreo de Humedad y Temperatura</title>
 	<link href="<?php echo base_url();?>css/general.css" media="screen,print" rel="stylesheet" type="text/css" />
 	
 	<script src="<?php echo base_url();?>js/highcharts.js" ></script>
 	<script src="<?php echo base_url();?>js/modules/exporting.js" type="text/javascript" ></script>
 	
 	
	<!-- <script src="http://code.highcharts.com/highcharts.js"></script>
	<script src="http://code.highcharts.com/modules/exporting.js"></script> -->
	



</head>
<script type="text/javascript">
var chart;
	$(document).ready(function() {
		var fechas1 = new Array();
		var temperaturas1 = new Array();
		var humedades1 = new Array();
		var n1=$("#cant_reg1").val();

		var fechas2 = new Array();
		var temperaturas2 = new Array();
		var humedades2 = new Array();
		var n2=$("#cant_reg2").val();


		//console.log(n);
		for (var i = 0; i < n1 ; i++) {
			fechas1[i]=$("#fecha1-"+i).val();
			temperaturas1[i]=parseFloat($("#temp1-"+i).val());
			humedades1[i]=parseFloat($("#hum1-"+i).val());
		}

		for (var i = 0; i < n2 ; i++) {
			fechas2[i]=$("#fecha2-"+i).val();
			temperaturas2[i]=parseFloat($("#temp2-"+i).val());
			humedades2[i]=parseFloat($("#hum2-"+i).val());
		}

		//console.log(temperaturas);

		chart = new Highcharts.Chart({
			chart: {
				renderTo: 'graficoTemp1', 	// Le doy el nombre a la gráfica
				defaultSeriesType: 'line'	// Pongo que tipo de gráfica es
			},
			title: {
				text: 'Datos de Temperatura'	// Titulo (Opcional)
			},
			subtitle: {
				text: 'Mes Actual'		// Subtitulo (Opcional)
			},
			// Pongo los datos en el eje de las 'X'
			xAxis: {
				categories: fechas1,
				// Pongo el título para el eje de las 'X'
				title: {
					text: 'Fechas'
				}
			},
			yAxis: {
				// Pongo el título para el eje de las 'Y'
				title: {
					text: 'Temperatura [°C]'
				}
			},
			// Doy formato al la "cajita" que sale al pasar el ratón por encima de la gráfica
			tooltip: {
				enabled: true,
				formatter: function() {
					return '<b>'+ this.series.name +'</b><br/>'+
						this.x +': '+ this.y +' '+this.series.name;
				}
			},
			// Doy opciones a la gráfica
			plotOptions: {
				line: {
					dataLabels: {
						enabled: false
					},
					enableMouseTracking: true
				}
			},
			// Doy los datos de la gráfica para dibujarlas
			series: [{
		                name: 'Temperatura',
		                data: temperaturas1
		            }],
		});	
	chart2 = new Highcharts.Chart({
			chart: {
				renderTo: 'graficoHum1', 	// Le doy el nombre a la gráfica
				defaultSeriesType: 'line'	// Pongo que tipo de gráfica es
			},
			title: {
				text: 'Datos de Humedad'	// Titulo (Opcional)
			},
			subtitle: {
				text: 'Mes Actual'		// Subtitulo (Opcional)
			},
			// Pongo los datos en el eje de las 'X'
			xAxis: {
				categories: fechas1,
				// Pongo el título para el eje de las 'X'
				title: {
					text: 'Fechas'
				}
			},
			yAxis: {
				// Pongo el título para el eje de las 'Y'
				title: {
					text: 'Humedad [%]'
				}
			},
			// Doy formato al la "cajita" que sale al pasar el ratón por encima de la gráfica
			tooltip: {
				enabled: true,
				formatter: function() {
					return '<b>'+ this.series.name +'</b><br/>'+
						this.x +': '+ this.y +' '+this.series.name;
				}
			},
			// Doy opciones a la gráfica
			plotOptions: {
				line: {
					dataLabels: {
						enabled: false
					},
					enableMouseTracking: true
				}
			},
			// Doy los datos de la gráfica para dibujarlas
			series: [{
		                name: 'Humedad',
		                data: humedades1
		            }],
		});	
	chart3 = new Highcharts.Chart({
			chart: {
				renderTo: 'graficoTemp2', 	// Le doy el nombre a la gráfica
				defaultSeriesType: 'line'	// Pongo que tipo de gráfica es
			},
			title: {
				text: 'Datos de Temperatura'	// Titulo (Opcional)
			},
			subtitle: {
				text: 'Mes Anterior'		// Subtitulo (Opcional)
			},
			// Pongo los datos en el eje de las 'X'
			xAxis: {
				categories: fechas2,
				// Pongo el título para el eje de las 'X'
				title: {
					text: 'Fechas'
				}
			},
			yAxis: {
				// Pongo el título para el eje de las 'Y'
				title: {
					text: 'Temperatura [°C]'
				}
			},
			// Doy formato al la "cajita" que sale al pasar el ratón por encima de la gráfica
			tooltip: {
				enabled: true,
				formatter: function() {
					return '<b>'+ this.series.name +'</b><br/>'+
						this.x +': '+ this.y +' '+this.series.name;
				}
			},
			// Doy opciones a la gráfica
			plotOptions: {
				line: {
					dataLabels: {
						enabled: false
					},
					enableMouseTracking: true
				}
			},
			// Doy los datos de la gráfica para dibujarlas
			series: [{
		                name: 'Temperatura',
		                data: temperaturas2
		            }],
		});	
	chart4 = new Highcharts.Chart({
			chart: {
				renderTo: 'graficoHum2', 	// Le doy el nombre a la gráfica
				defaultSeriesType: 'line'	// Pongo que tipo de gráfica es
			},
			title: {
				text: 'Datos de Humedad'	// Titulo (Opcional)
			},
			subtitle: {
				text: 'Mes Anterior'		// Subtitulo (Opcional)
			},
			// Pongo los datos en el eje de las 'X'
			xAxis: {
				categories: fechas2,
				// Pongo el título para el eje de las 'X'
				title: {
					text: 'Fechas'
				}
			},
			yAxis: {
				// Pongo el título para el eje de las 'Y'
				title: {
					text: 'Humedad [%]'
				}
			},
			// Doy formato al la "cajita" que sale al pasar el ratón por encima de la gráfica
			tooltip: {
				enabled: true,
				formatter: function() {
					return '<b>'+ this.series.name +'</b><br/>'+
						this.x +': '+ this.y +' '+this.series.name;
				}
			},
			// Doy opciones a la gráfica
			plotOptions: {
				line: {
					dataLabels: {
						enabled: false
					},
					enableMouseTracking: true
				}
			},
			// Doy los datos de la gráfica para dibujarlas
			series: [{
		                name: 'Humedad',
		                data: humedades2
		            }],
		});	
	});
</script>
<style type="text/css">

</style>



<body>
	<div class="container"><h2>Graficos del Mes Actual:</h2></div>
	<div id="graficoTemp1" style="width: 100%; height: 500px; margin: 0 auto"></div>
	<br></br>

	<div id="graficoHum1" style="width: 100%; height: 500px; margin: 0 auto"></div>

	<br>
	<br>

	<div class="container"><h2>Graficos del Mes Anterior:</h2></div>
	<div id="graficoTemp2" style="width: 100%; height: 500px; margin: 0 auto"></div>
	<br></br>

	<div id="graficoHum2" style="width: 100%; height: 500px; margin: 0 auto"></div>

<?php
$cant_reg1=count($datos["datos_actual"]);
echo "<input type='text' id='cant_reg1' name='cant_reg1' value='".$cant_reg1."' hidden>";
for ($i=0; $i < $cant_reg1; $i++) { 
		echo "<input type='text' id='id1-".$i."' name='id1-".$i."' value='".$datos["datos_actual"][$i]["id"]."' hidden>";
		echo "<input type='text' id='temp1-".$i."' name='temp1-".$i."' value='".$datos["datos_actual"][$i]["temperatura"]."' hidden>";
		echo "<input type='text' id='hum1-".$i."' name='hum1-".$i."' value='".$datos["datos_actual"][$i]["humedad"]."' hidden>";
		echo "<input type='text' id='fecha1-".$i."' name='fecha1-".$i."' value='".$datos["datos_actual"][$i]["cuando"]."' hidden>";
	}
$cant_reg2=count($datos["datos_anterior"]);
echo "<input type='text' id='cant_reg2' name='cant_reg2' value='".$cant_reg2."' hidden>";
for ($i=0; $i < $cant_reg2; $i++) { 
		echo "<input type='text' id='id2-".$i."' name='id2-".$i."' value='".$datos["datos_anterior"][$i]["id"]."' hidden>";
		echo "<input type='text' id='temp2-".$i."' name='temp2-".$i."' value='".$datos["datos_anterior"][$i]["temperatura"]."' hidden>";
		echo "<input type='text' id='hum2-".$i."' name='hum2-".$i."' value='".$datos["datos_anterior"][$i]["humedad"]."' hidden>";
		echo "<input type='text' id='fecha2-".$i."' name='fecha2-".$i."' value='".$datos["datos_anterior"][$i]["cuando"]."' hidden>";
	}
	?> 
</body>



