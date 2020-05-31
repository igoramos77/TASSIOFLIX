// select the strip
$('section').each(function() {

  // change the number of the 'li' elements and the strip will be fine anyway
  
  var wUl = $(this).find('ul').width();
  var nLi = $(this).find('ul').children().length;
  var wElement = 100 / nLi;

  $('li').css('width', wElement + '%');
  
  // hover 'li'

  $(this).find('li').hover(

    // mouse In
    function() {
      $(this).toggleClass('hover');

      var scaleFactor = 1.8;
      var wBigElement = $(this).width() * scaleFactor;
      var translation = (wBigElement - $(this).width()) / 2;
      
      var item = $(this).parent().children();

      $(this).css('transform', 'scale(' + scaleFactor + ')');
      
      if ($(this).is(':nth-child(1)')) {
        item.slice(1,nLi).css('transform', 'translate(' + translation * 2 + 'px,  0px)');
      } 

        for (var i = 2; i <= nLi - 1; i++) {
          if ($(this).is(':nth-child(' + i + ')')) {
            item.slice(0,i-1).css('transform', 'translate(-' + translation + 'px,  0px)')
             .end().slice(i).css('transform', 'translate(' + translation + 'px,  0px)');
          } 
        }

      if ($(this).is(':nth-child(' + nLi + ')')) {
        item.slice(0,(nLi-1)).css('transform', 'translate(-' + translation * 2 + 'px,  0px)');
      }   

    // mouse Out
    }, function() {
        $(this).toggleClass('hover');
        $(this).css('transform', 'scale(1)');
        $('li').not(this).css('transform', 'translate(0px,  0px)');
    }
  );
});

$('.carousel').carousel({
  interval: 30000,
  touch: true,
  autoplay: false,
  cycle: true
})


//load spin after click play btn
$('.play-button').click(function() {
  $(this).hide();
  $('.spin').fadeIn();
  $('html, body').css('overflow', 'hidden'); 
  $('.carousel-caption, .carousel-indicators, .navbar').hide();
  $('.bg-fade').addClass('bg-dark');


  var vid = document.querySelector("#player"); 
  vid.play(); 
});

//get modal close
$('#player-modal').on('hidden.bs.modal', function () {
  var vid = document.querySelector("#player"); 
  vid.pause(); 
  setTimeout(() => {
    $('.spin').fadeOut();
    $('.play-button').show();
    $('.bg-fade').removeClass('bg-dark')
    $('html, body').css('overflow', 'visible'); 
    $('.carousel-caption, .carousel-indicators, .navbar').show();
  }, 800);
})

// modal search open btn
$('.search-icon').click(function() {
  $('.search-blur').fadeIn();
  $('html, body').css('overflow', 'hidden'); 
});

// modal search close btn
$('.close-btn').click(function() {
  $('.search-blur').fadeOut();
  $('html, body').css('overflowY', 'visible'); 
});


// Menu change bg
$(window).on('scroll',function() {    
  var scroll = $(window).scrollTop();
  if (scroll < 20) {
   $('.navbar').removeClass('bg-dark');   
  }
  else {
    $('.navbar').addClass('bg-dark');
  }
});
