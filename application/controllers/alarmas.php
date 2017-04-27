<?php
class alarmas extends CI_Controller {
	public function __construct()
	{
		parent::__construct();
	}

   public function index()
   {

   	$datos["alertas"]=$this->data_model->Alertas();

   	$data['section_title']='Alertas del sistema';

		$data['layout_navigation']=$this->load->view('layout_navigation',NULL,TRUE);

		$data['layout_body']=$this->load->view('alertas',array("datos"=>$datos),TRUE);

		$this->load->view('layout_sin_sidebar',array("data"=>$data),FALSE);
	//exit();
	
    }

   

    }
?>
