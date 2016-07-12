$(function(){
  $("#search").keyup(function(){
    var search = $("#search").val();
    $.ajax({
      type:"post",
      url:"search.php",
      data:{"search":search},
      success: function(response){
        $("#demo").html(response);
      }
    });
    return false;
  });
});
