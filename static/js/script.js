$(document).ready(function(){
    $(".sidenav").sidenav({edge:"right"});
  });

/*
------------------------------------------
Display current year in Footer copyright 
------------------------------------------
*/

$("#year").html(new Date().getFullYear());