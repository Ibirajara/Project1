$(document).ready(function(){
	$('.campo_moeda').mask('999999990.00', {reverse: true});
	$('.date_mask').mask('00/00/0000', {placeholder: '__/__/____'}, );
	$('.cpf').mask('###.###.###-##',  {placeholder: '___.___.___-__'}, );
	$('.phone').mask('(00) 00000-0000', {placeholder: '(__) _____-____'}, );
});