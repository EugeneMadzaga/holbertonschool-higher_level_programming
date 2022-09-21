$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else if ($('HEADER').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
