<?php
class graficos extends CI_Controller {
	public function __construct()
	{
		parent::__construct();
	}

   public function index()
   {


   	

    $ahora = strtotime("Now");
    $anterior = strtotime("-1 month", $ahora);


    $hasta_actual= date("Y-m-31",$ahora);
    $desde_actual= date("Y-m-01",$ahora);

    $datos["desde_actual"]=$desde_actual;
    $datos["hasta_actual"]=$hasta_actual;

    $hasta_anterior= date("Y-m-31",$anterior);
    $desde_anterior= date("Y-m-01",$anterior);

    $datos["desde_anterior"]=$desde_anterior;
    $datos["hasta_anterior"]=$hasta_anterior;
/*
   	echo $desde_actual;
   	echo "</br>";
   	echo $hasta_actual;
    echo "</br>";
    echo $desde_anterior;
    echo "</br>";
    echo $hasta_anterior;
    echo "</br>";
   	exit(); */
   	//$datos["datos"]=$this->data_model->Datos();
   	$datos["datos_actual"]=$this->data_model->DatosFiltrados2($desde_actual,$hasta_actual);
    $datos["datos_anterior"]=$this->data_model->DatosFiltrados2($desde_anterior,$hasta_anterior);
   	//print_r($datos);exit();

    $data['section_title']='Sistema de Monitoreo';

    $data['layout_navigation']=$this->load->view('layout_navigation',NULL,TRUE);

    $data['layout_body']=$this->load->view('graficos',array("datos"=>$datos),TRUE);

    $this->load->view('layout_sin_sidebar',array("data"=>$data),FALSE);
	
    }

   

    }
?>
