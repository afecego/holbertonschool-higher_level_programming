const $ = window.jQuery;
window.onload = function () {
  $(document).ready(function () {
    $('DIV#toggle_header').click(function () {
      $('header').toggleClass('green red');
    });
  });
};
