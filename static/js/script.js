$(document).ready(function(){
    $(".sidenav").sidenav({edge:"right"});
    $('select').formSelect();
    $('.modal').modal();
  });

/*
------------------------------------------
Display current year in Footer copyright 
------------------------------------------
*/

$("#year").html(new Date().getFullYear());