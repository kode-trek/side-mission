void sim_ena(string arg1, string arg2) {
	//var(s)
 	string dname = (string) arg1 + "/";
	unsigned long long int N = 0;
	unsigned long long int n = 0;
	if (arg2 == "") N = 1;
	else N = str2num(arg2);
	vector<string> list = {};
	string tdname = ts();
	string target = "";
	string source = "";
	//op(s)
	list = tree(dname, false);
	cd(dname);
	n = N;
	for(int i = 0; i < list.size(); i++) {
		if (dir(list[i])) continue;
		else n++;
	}
	cout <<
	"[...] creates " << quote(tdname) << " directory inside " << quote(dname) <<
	".""\n"
	"[...] move file(s) within " << quote(dname) << " to " << quote(tdname) <<
	".""\n"
	"[...] enumerating them: " << N << "~" << n - 1 << ".""\n"
	"[...] replaces them back to " << quote(dname) << ".""\n"
	"[...] removes " << quote(tdname)
	<< endl;
}
