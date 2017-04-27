<?php
class configuracion extends CI_Controller {
	public function __construct()
	{
		parent::__construct();
	}

   public function index()
   {

   	$datos["limites"]=$this->data_model->CargarLimites();
   	//print_r($datos);exit();

   	$data['section_title']='Configuración del Sistema';

		$data['layout_navigation']=$this->load->view('layout_navigation',NULL,TRUE);

		$data['layout_body']=$this->load->view('configuracion',array("datos"=>$datos),TRUE);

		$this->load->view('layout_sin_sidebar',array("data"=>$data),FALSE);
	//exit();
	
    }

    function guardar(){
    	$t_min=$this->input->post('t_min');
    	$t_max=$this->input->post('t_max');
    	$h_min=$this->input->post('h_min');
    	$h_max=$this->input->post('h_max');

    	$this->data_model->ActualizarLimites($t_min,$t_max,$h_min,$h_max);
    	redirect('/registros', 'refresh');

    }

    function borrar_registros(){
      $this->data_model->BorrarRegistros();
      redirect('/registros', 'refresh');
    }

    function borrar_alertas(){
      $this->data_model->BorrarAlertas();
      redirect('/registros', 'refresh');
    }

    function agendar(){
      $email=$this->input->post("email");
      $n=$this->data_model->CheckCorreo($email);
      if($n==0){
        $this->data_model->AgregarCorreo($email);
      }
      redirect('/registros', 'refresh');
    }

   

    }
?>
