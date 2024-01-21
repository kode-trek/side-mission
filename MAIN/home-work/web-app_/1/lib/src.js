// disables ENTER-key
window.addEventListener('keydown', function(e) {
	if (
			e.keyIdentifier == 'U+000A' ||
			e.keyIdentifier == 'Enter' ||
			e.keyCode == 13
	) {
			if (e.target.nodeName == 'INPUT' && e.target.type == 'text') {
				e.preventDefault()
				return false
			}
	}
}, true)

function Pinger_ping(ip, callback) {

  if(!this.inUse) {

    this.inUse = true;
    this.callback = callback
    this.ip = ip;

    var _that = this;

    this.img = new Image();

    this.img.onload = function() {_that.good();};
    this.img.onerror = function() {_that.good();};

    this.start = new Date().getTime();
    this.img.src = "http://" + ip;
    this.timer = setTimeout(function() { _that.bad();}, 1500);

  }
}
