
$(document).ready(function(){

	// show/hide du formulaire de création d'un portefeuille
	$('#btn_create_ptf').click(function() {
		// TODO disabler le bouton
		$('#div_form_create_ptf').show();
	});
	
	// submit async du formulaire de création d'un portefeuille
	$('#form_create_ptf').submit(function() {
	  alert('Submition du formulaire de création de portefeuille !');
	  // TODO raz le form et le hider, re-enabler le bouton de création
	  return false;
	});
	
});