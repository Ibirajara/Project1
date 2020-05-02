$(document).ready(function(){
	$('.campo_moeda').mask('999999990.00', {reverse: true});
	$('.date_mask').mask('00/00/0000');
	$('.cpf').mask("###.###.###-##",  {placeholder: '___.___.___-__'}, );
});