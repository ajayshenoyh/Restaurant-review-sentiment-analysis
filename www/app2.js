var main = function() {
$('#s1').click(function(){
if($('input[name=aspect]:checked').length<=0)
   {
    alert("Select an aspect")
   }
 });
 $('#b3').click(function(){
    window.location.href='Index.html';
	});
}
$(document).ready(main);