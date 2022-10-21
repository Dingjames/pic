# Created by ndiritumetasploit

import os

print("""<style>  
body {background-color:black;}  

img{position:absolute;
top:0px;left:0px;
max-width:device-width;opacity:0;filter:grayscale(100%);z-index:-2;
}

</style>""")

print("""<h2 id="h2" style="text-align:center;font-family:cursive;position:relative;top:-40px;">Happy New Year!</h2>
<script>
window.onload = myFunction;
function myFunction() {
document.getElementsByTagName("img")[0].style.display = "none"; 
var tiger = document.getElementsByTagName("img");
tiger[1].style.opacity = "1"; 
tiger[1].style.transitionDuration = "15s"; 
        var myVar = setInterval(myVib, 3000);
 
function myVib(){let i = 50;
let id = setInterval(function() {
    i--;    
    if (i == -1) {
        clearInterval(id);     
    } else {    
navigator.vibrate&&navigator.vibrate(16); 
    }
}, 50);  

//the stop function

function stopVib() {
  clearInterval(myVar);  
  tiger[1].style.filter = "grayscale(0%)";
  var happy = document.getElementById("h2");
happy.innerHTML = "Greetings all!";
happy.style.color = "goldenrod";
happy.style.transitionDuration = "3s";

}
setTimeout(stopVib, 3000);
       
};        
    }
</script>""")

os.system("touch file.png")

import urllib.request as cat
url = 'https://i.ibb.co/p3NySHK/1666365329181.jpg'
cat.urlretrieve(url, 'cat.png');
