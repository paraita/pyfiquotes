
$(document).ready(function(){

	// ----------------- PORTFOLIO RELATED ---------------
	
	// création d'un nouveau portefeuille
	$('#form_create_ptf').submit(function() {
		$.ajax({
			url: "/ptf?action=create_ptf&name=" + $('#ptf_name').val(),
			cache: false
		}).done(function(html) {
			$('#div_form_create_ptf').hide();
			$('#btn_create_ptf').removeClass('disabled');
			$('#ptf_name').val('');
			// mettre le bon morceau qui m'interesse
			caca = html;
			$('#portfolios').html($(html).find('#portfolios'));
		});
		return false;
	});
	
	// suppression d'un portefeuille
	// TODO demander confirmation
	$(".action_delete").click(function(event) {
		$.ajax({
			url: "/ptf?action=del_ptf&ptf=" + event.target.id.replace('action_', ''),
			cache: false
		}).done(function(html) {
			$('#div-' + html).remove();
		});
		return false;
	});
	
	// show du formulaire de création d'un portefeuille
	$('#btn_create_ptf').click(function() {
		$('#div_form_create_ptf').show();
		$('#btn_create_ptf').addClass('disabled');
	});
	
	// hide du formulaire de création d'un portefeuille
	$('#btn_hide_ptf_form').click(function() {
		$('#div_form_create_ptf').hide();
		$('#btn_create_ptf').removeClass('disabled');
		$('#ptf_name').val('');
	});
	
	
	// ----------------- ASSET RELATED ---------------
	
	// déclaration d'un nouvel asset
	$('#form_declare_asset').submit(function() {
		$.ajax({
			url: "/ptf?action=declare_asset&" +
				 "label=" + $('#asset_label').val() + "&" +
				 "symbol=" + $('#asset_symbol').val() + "&" +
				 "isin=" + $('#asset_isin').val() + "&" +
				 "market=" + $('#asset_market').val() + "&" +
				 "curr=" + $('#asset_curr').val() + "&" +
				 "type=" + $('#asset_type').val(),
			cache: false
		}).done(function(html) {
			$('#div_form_declare_asset').hide();
			$('#btn_declare_asset').removeClass('disabled');
			$('#asset_label').val('');
			$('#asset_symbol').val('');
			$('#asset_isin').val('');
			$('#asset_market').val('');
			$('#asset_curr').val('');
			$('#asset_type').val('');
			// mettre le bon morceau qui m'interesse
			caca = html;
			$('#div-assets').html($(html).find('#div-assets'));
		});
		return false;
	});
	
	// show du formulaire de déclaration d'un titre
	$('#btn_declare_asset').click(function() {
		$('#div_form_declare_asset').show();
		$('#btn_declare_asset').addClass('disabled');
	});
	
	// hide du formulaire de déclaration d'un titre
	$('#btn_hide_asset_form').click(function() {
		$('#div_form_declare_asset').hide();
		$('#btn_declare_asset').removeClass('disabled');
		$('#asset_label').val('');
		$('#asset_symbol').val('');
		$('#asset_isin').val('');
		$('#asset_market').val('');
		$('#asset_curr').val('');
		$('#asset_type').val('');
	});

});

var caca;