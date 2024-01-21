var x = document.getElementById("id1").innerHTML;
setInterval(function(){window.location = "writer.php?data=" + x;}, 1000);
