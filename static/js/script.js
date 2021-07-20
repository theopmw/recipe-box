$(document).ready(function(){
    $(".sidenav").sidenav({edge:"right"});
    $('select').formSelect();
  });

/*
------------------------------------------
Display current year in Footer copyright 
------------------------------------------
*/

$("#year").html(new Date().getFullYear());