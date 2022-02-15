const $ = window.jQuery;
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $('header').css('background', '#FF0000');
  });
});
