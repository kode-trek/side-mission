void sim_cdup(string arg1) {
	//var(s)
	if (arg1 == "") arg1 = pwd();
	string d = (string) arg1 + "/";
	//op(s)
	cout <<
	"[...] ignores folder(s) inside " + quote(d) + ".""\n"
	"[...] creates folder(s) with common file-size as their name(s).""\n"
	"[...] eliminates clusters with only 1 item."
	<< endl;
}
