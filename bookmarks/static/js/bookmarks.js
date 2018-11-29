// delete bookmark ajax function
function delete_bookmark(bm_id) {
    var csrftoken = Cookies.get('csrftoken');
    ajax_url = "/bookmarks/delete-bookmark/"
    $.ajaxSetup({
        crossDomain: false,
        beforeSend: function(xhr, settings) {
	    xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    $.ajax({
      type:"POST",
      async: true,
      url: ajax_url,
      data: {
        bmid: bm_id
      },
      success: function(data){
        setTimeout(function(){
          location.reload();
        }, 200);
      },
      error : function(request, error){
        console.log("ERROR:"+ error);
      }
    });
}

// delete bookmark on click
$(document).ready(function() {
  $(".delete-bm").on('click', function(e){
    e.preventDefault();
    bm_id = $(this).data('bmid');
    delete_bookmark(bm_id);
  })
});
