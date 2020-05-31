// select the strip

$("section").each(function() {

  // change the number of the "li" elements and the strip will be fine anyway
  
  var wUl = $(this).find("ul").width();
  var nLi = $(this).find("ul").children().length;
  var wElement = 100 / nLi;

  $("li").css("width", wElement + "%");
  
  // hover "li"

  $(this).find("li").hover(

    // mouse In
    function() {
      $(this).toggleClass("hover");

      var scaleFactor = 1.8;
      var wBigElement = $(this).width() * scaleFactor;
      var translation = (wBigElement - $(this).width()) / 2;
      
      var item = $(this).parent().children();

      $(this).css("transform", "scale(" + scaleFactor + ")");
      
      if ($(this).is(":nth-child(1)")) {
        item.slice(1,nLi).css("transform", "translate(" + translation * 2 + "px,  0px)");
      } 

        for (var i = 2; i <= nLi - 1; i++) {
          if ($(this).is(":nth-child(" + i + ")")) {
            item.slice(0,i-1).css("transform", "translate(-" + translation + "px,  0px)")
             .end().slice(i).css("transform", "translate(" + translation + "px,  0px)");
          } 
        }

      if ($(this).is(":nth-child(" + nLi + ")")) {
        item.slice(0,(nLi-1)).css("transform", "translate(-" + translation * 2 + "px,  0px)");
      }   

    // mouse Out
    }, function() {
        $(this).toggleClass("hover");
        $(this).css("transform", "scale(1)");
        $("li").not(this).css("transform", "translate(0px,  0px)");
    }
  );
});