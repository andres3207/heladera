<?php
 class data_model extends CI_Model
 {

 	function Datos(){
 		$consulta="SELECT * From datos WHERE ocultar=0 order by cuando desc";
 		$query = $this->db->query($consulta);
 		return $query->result_array();
 	}

 	function DatosFiltrados($desde,$hasta){
 		$consulta="SELECT * From datos WHERE (date(cuando)>='".$desde."' and date(cuando) <= '".$hasta."' and ocultar=0) order by cuando desc";
 		//echo $consulta;
 		//exit();
 		$query = $this->db->query($consulta);
 		return $query->result_array();
 	}
 	function DatosFiltrados2($desde,$hasta){
 		$consulta="SELECT * From datos WHERE (date(cuando)>='".$desde."' and date(cuando) <= '".$hasta."') order by cuando asc";
 		//echo $consulta;
 		//exit();
 		$query = $this->db->query($consulta);
 		return $query->result_array();
 	}
 	function Alertas(){
 		$consulta="SELECT * from alertas WHERE ocultar=0 order by cuando desc";
 		$query = $this->db->query($consulta);
 		return $query->result_array();
 	}

 	function ActualizarLimites($t_min,$t_max,$h_min,$h_max){
 		$consulta="UPDATE configuracion set t_min='".$t_min."',t_max='".$t_max."',h_min='".$h_min."',h_max='".$h_max."' WHERE id=1";
 		$query = $this->db->query($consulta);
 		//return $query->result_array();
 	}
 	function CargarLimites(){
 		$consulta="SELECT t_min,t_max,h_min,h_max From configuracion WHERE id=1";
 		$query = $this->db->query($consulta);
 		return $query->row_array();
 	}

 	function BorrarRegistros(){
 		$consulta="UPDATE datos set ocultar=1, cuando=cuando where 1";
 		$query = $this->db->query($consulta);
 	}
 	function BorrarAlertas(){
 		$consulta="UPDATE alertas set ocultar=1, cuando=cuando where 1";
 		$query = $this->db->query($consulta);
 	}
 	function AgregarCorreo($email){
 		$consulta="INSERT INTO correos (email,habilitado) values ('".$email."',1)";
 		$query = $this->db->query($consulta);
 	}
 	function CheckCorreo($email){
 		$consulta="SELECT COUNT(id) from correos where email='".$email."'";
 		$query = $this->db->query($consulta);
 		return array_values($query->row_array())[0];
 	}
	
 }
 ?>
