$("#submit").click(function(){
    item_selected = $('#sel1').find(":selected").val()
    $.ajax({
      type: 'POST',
      url: "/refresh",
      data: {input: item_selected},
      dataType: "text",
      success: function(data){
                 alert("Deleted Student ID "+ student_id.toString());
               }
    });
});