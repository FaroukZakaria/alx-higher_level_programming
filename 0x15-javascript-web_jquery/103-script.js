$(document).ready(function(){
$('INPUT#btn_translate, INPUT#language_code').on('click keypress', function(event){
    if (event.type === 'click' || (event.type === 'keypress' && event.which === 13)) {
        const languageCode = $('INPUT#language_code').val();
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            data: { lang: languageCode },
            method: 'GET',
            success: function(response) {
                $('DIV#hello').text(response.hello);
            },
            error: function(error) {
                console.error(error);
            }
        });
    }
});
});
