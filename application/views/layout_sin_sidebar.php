<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8;charset=utf-8" />
    <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
	<title>Sistema de Monitoreo de Humedad y Temperatura</title>
	 <link href="<?php echo base_url();?>css/general.css" media="screen" rel="stylesheet" type="text/css" /> 
	<!--<link href="<?php echo base_url();?>css/imprimir.css" media="print" rel="stylesheet" type="text/css" />    
    <link href="<?php echo base_url();?>css/form.css" type="text/css" rel="stylesheet" media="screen" /> -->
    <link href="<?php echo base_url();?>css/menu.css" type="text/css" rel="stylesheet" media="screen" />
   <!-- <link href="<?php echo base_url();?>css/styles.css" type="text/css" rel="stylesheet" media="screen" />-->
	<script src="<?php echo base_url();?>js/jquery-1.7.2.js" type="text/javascript" ></script>
    <script src="<?php echo base_url();?>js/jquery.validate.min.js" type="text/javascript" ></script>
   <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->

   <link href="<?php echo base_url();?>css/bootstrap.min.css" rel="stylesheet" />
  <!-- <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css"> -->
  <script src="<?php echo base_url();?>js/bootstrap.min.js" ></script>
  <!--<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>-->

<!--<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"> -->
</head>
<body>
<div class="contenedor">
<!--begin:nave_page-->
<header>
   <nav style="background:#F3F3F3 ;"> 
    <!--   <nav style="
  background: red; 
  background: -webkit-linear-gradient(blue,blue,red); 
  background: -o-linear-gradient(white,blue,red);
  background: -moz-linear-gradient(blue,white,red);  
  background: linear-gradient(LightSkyBlue,Gainsboro);
 "> -->
 
 <!--      <div class="top" align="center">


           
<img class="img-responsive" src="<?php echo base_url();?>img/header.jpg" width="1200" height="10"></div>--> 

   
        <div id="navi" class="container_16" style="width: 80%; margin: 0 auto !important; min-width: 1200px !important;"> 
        <?php //echo $layout_navigation;
echo $data['layout_navigation'] ;        ?>
        
        </div>
    </nav>
</header>
<!--end:nav_page-->
<!--begin:page_title-->
<div id="company-content">
<div class="wrapper clearfix">
<div id="section-header" class="clearfix">
          </br><h1><?php
	echo $data['section_title'] ;            
          ?></h1>
        </div>
</div>
<!--end:page_title-->
<div id='company-support-portal'>
<div class='wrapper'>
<!--begin:body-->
<div id="support-main" class="columnas2">
	<!--begin:content-->
  	<div class='support-body' style="padding:10px">
    
     <?php //echo $layout_body;
		echo $data['layout_body'] ;                 
     ?>
   
	</div>
    <!--end:content-->
    <!--begin:footer  delete-api-button.png

-->
<div id='footer' style="height:170px; width:100%;">
    <h5 style='margin-top: 75px;padding:20px;'>	TECNOCADA  
	Av. Brown 2650, Olavarria. Buenos Aires. Argentina. <br />

Consultas: Tel: (02284) 15652604 - TECNOCADA@hotmail.com
        </h5>
        
    </div>
	<!--end:footer-->
</div>
</div>
</div>
</div>

</div>
</body>
</html>
