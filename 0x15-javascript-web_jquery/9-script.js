const $ = window.jQuery;
$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
    if (textStatus === 'success') {
      $('DIV#hello').html(data.hello);
    }
  });
});
