$(document).scroll(function() {
    var y = $(this).scrollTop();
    if (y > 50) {
      $('.navbar')
        .css({
          'visibility':'hidden',
        });
    } else {
      $('.navbar')
        .css({
          'visibility': 'visible',
        });
    }
  });
