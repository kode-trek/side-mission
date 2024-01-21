//disable-ENTER-key --
window.addEventListener(
'keydown',
function(e) {
	if(e.keyIdentifier == 'U+000A' || e.keyIdentifier == 'Enter' || e.keyCode == 13) {
		if(e.target.nodeName == 'INPUT' && e.target.type == 'text') {
			e.preventDefault()
			return false
		}
	}
},
true
)

function f1() {
	var v1 = document.getElementById('id1').value;
	var v2 = document.getElementById('id2').value;
	var w = "";
	w += "name: " + v1; w += '\n';
	w += "age: " + v2; w += '\n';
	w += '\n';
	document.getElementById('id3').value += w;
//
	var u = "";
	u += "name=" + v1;	u += '\n';
	u += "age=" + v2;		u += '\n';
	document.getElementById('id4').value += u;
}
