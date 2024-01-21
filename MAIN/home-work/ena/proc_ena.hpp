void proc_ena(string arg1, string arg2) {
	//var(s)
 	string dname = arg1 + "/";
	if (not dir(dname)) {
		cout << "directory not found: " << quote(dname) << endl;
		exit(1);
	}
	if (not write_access(dname)) {
		cout << "write-permission denied." << endl;
		exit(1);
	}
	unsigned long long int N = 0;
	unsigned long long int n = 0;
	if (arg2 == "") N = 1;
	else N = str2num(arg2);
	vector<string> list = {};
	string tdname = ts();
	string source = "";
	string target = "";
	//op(s)
	cd(dname);
	list = tree();
	md(tdname);
	n = N;
	for(int i = 0; i < list.size(); i++) {
		if (dir(list[i])) continue;
		else {
			source = list[i];
			target = tdname + "/" + str(n) + uri(list[i])[3];
			mv(source, target);
			n++;
		}
	}
	list = tree(tdname);
	for(int i = 0; i < list.size(); i++) {
		source = list[i];
		target = pwd();
		mv(source, target);
	}
	rm(tdname);
	cout << "[OK] file(s) renamed: " << N << "~" << n - 1 << endl;
}
