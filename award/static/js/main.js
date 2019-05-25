$(document).ready(function() {
  $("#love").click(function(){
    $("#love").hide()
    $(".form").slideDown(2000)
      $(".form").show()

  })

  // $("#send").submit(function(event) {
  //   event.preventDefault()
  //   form=$("#send")
  //
  //   $.ajax({
  //     'url':'/ajax/review/',
  //     'type':'POST',
  //     'data':form.serialize(),
  //     'dataType':'json',
  //     'success':function(data) {
  //       $("#alert").text(data['success'])
  //
  //     },
  //
  //   })
  //   $(".form").hide()
  //   $("#alert").show()
  //
  //
  // })

})
