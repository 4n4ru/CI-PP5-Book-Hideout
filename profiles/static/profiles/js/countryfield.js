let countySelected = $('#id_default_country').val();
if(!countySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}
$('#id_default_country').change(function(){
    countySelected = $(this).val();
    if(!countySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});