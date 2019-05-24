$(document).ready(function(){
  $("#test").click(function(){
    alert("success")
  })
  $("#clickSearch").click(function(){
    $("#search").fadeIn(2000)
    $("#search").show()
  })
  // $("#copy").click(function(){
  //   alert("done")
  //
  //   $("#paste").show()
  // })
  // $("#paste").click(function(){
  //   $("#copy").hide()
  // })
  $(function () {
$('[data-toggle="popover"]').popover()
})
$('.popover-dismiss').popover({
trigger: 'focus'
})


})
function copyText(){
  var copytext=document.getElementById("copi");
  copytext.select();
  document.execCommand("copy")
}
function status(clickedBtn)
    {
      clickedBtn.value = "Copied to clipboard";
      clickedBtn.disabled = true;
      clickedBtn.style.color = 'white';
      clickedBtn.style.background = 'gray';

      //New Code
      copyToCliboard(clickedBtn.previousSibling);
    }
    function copyToCliboard(el) {
      if (document.body.createTextRange) {
          var range = document.body.createTextRange();
          range.moveToElementText(el);
          range.select();
      } else {
          var selection = window.getSelection();
          var range = document.createRange();
          range.selectNodeContents(el);
          selection.removeAllRanges();
          selection.addRange(range);
      }
      document.execCommand("copy");
      window.getSelection().removeAllRanges();
  }
