$(document).ready(function(){
    $(".sidenav").sidenav({edge:"right"});
    $('select').formSelect();
    $('.carousel.carousel-slider').carousel({
      fullWidth: true,
      indicators: true
    });
  });

/*
------------------------------------------
Display current year in Footer copyright 
------------------------------------------
*/

$("#year").html(new Date().getFullYear());