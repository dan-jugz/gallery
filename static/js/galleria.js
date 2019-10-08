var $grid = $('.grid').imagesLoaded( function() {
    $grid.masonry({
        itemSelector:'.grid-item',
        percentPosition:true,
        columnWidth:'.grid-sizer'
    });
  });

  $(function() {
    $("input").click(function() {
    $(this).focus();
    $(this).select();
    document.execCommand('copy');
    $(this).after("Copied link");
    });
   });