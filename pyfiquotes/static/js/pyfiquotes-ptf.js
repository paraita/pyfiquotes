
$(document).ready(function(){

	$(".action_delete").click(function(event) {
		$.ajax({
			url: "/ptf?action=del_ptf&ptf=" + event.target.id.replace('action_', ''),
			cache: false
		}).done(function(html) {
			$('#div-' + html).remove();
		});
		return false;
	});

	// création d'un nouveau portefeuille
	$('#form_create_ptf').submit(function() {
		$.ajax({
			url: "/ptf?action=create_ptf&name=" + $('#ptf_name').val(),
			cache: false
		}).done(function(html) {
			$('#div_form_create_ptf').hide();
			$('#btn_create_ptf').removeClass('disabled');
			// mettre le bon morceau qui m'interesse
			$('#portfolios').append(html);
		});
		return false;
	});
	
	// show/hide du formulaire de création d'un portefeuille
	$('#btn_create_ptf').click(function() {
		$('#div_form_create_ptf').show();
		$('#btn_create_ptf').addClass('disabled');
	});

});