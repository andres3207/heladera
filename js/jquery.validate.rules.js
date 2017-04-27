jQuery(document).ready(function() {
$("#registro").validate({
	rules: {
		"evaluador_apellido": { required: true },
		"evaluador_nombre"	: { required: true },
		"evaluador_dni"		: { required: true, number: true, minlength: 7 },	
		"evaluador_email"	: { required: true, email: true },
		"evaluador_email2"	: { required: true, email: true, equalTo: "#evaluador_email" },
		"e_titulo_grado"	: { required: true },
	},
	messages: {
		e_titulo_grado: "Por favor complete su título de grado",
		evaluador_apellido: "Por favor complete su apellido",
		evaluador_nombre: "Por favor complete su nombre",
		evaluador_dni: {
			required: "Por favor complete su DNI",
			number: "Por favor complete con solo números",
			minlength: "Su DNI debe tener como mínimo 7 dígitos"
			},
		evaluador_email: {
			required: "Por favor ingrese su email",
			email: "El mail ingresado no es válido"
			},
		evaluador_email2: {
			required: "Por favor ingrese su email nuevamente",
			email: "El mail ingresado no es válido",
			equalTo: "El mail ingresado debe ser igual al anterior"
			},
		},
	}); 	
});