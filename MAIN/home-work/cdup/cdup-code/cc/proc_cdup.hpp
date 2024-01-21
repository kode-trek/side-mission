void proc_cdup(string arg1) {
	//var
	string d = (string) arg1 + "/";
	if (not dir(d)) {
		cout << "directory not found:" << "\t" << quote(d) << endl;
		exit(1);
	}
	vector<string> list = tree(d, false);
	vector<string> unique_list = {};
	vector<int> size_list = {};
	//msg(s)
	string msg1 = "clustering file(s) by size...";
	//op(s)
	disp(msg1);
	// doesn't cluster folder(s)
	for(int i = 0; i < list.size(); i++) {
		if(dir(list[i])) continue;
		else unique_list.push_back(list[i]);
	}
	for(int i = 0; i < unique_list.size(); i++) {
		size_list.push_back(fsize(unique_list[i]));
		mkdir(d + to_string(fsize(unique_list[i])));
		mv(unique_list[i], d + to_string(fsize(unique_list[i])));
	}
	size_list = unique(size_list);
	// eliminates clusters with only 1 item
	for(int i = 0; i < size_list.size(); i++) {
		if (tree(d + to_string(size_list[i]), false).size() == 1) {
			mv(tree(d + to_string(size_list[i]), false)[0], d);
			rm(d + to_string(size_list[i]));
		}
		else mv(to_string(size_list[i]), d);
	}
	cout << "DONE." << endl;
}
