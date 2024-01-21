#include "proc_cdup.hpp"
#include "sim_cdup.hpp"

int main(int argc, char* argv[]) {
	if ((string) argv[1] == "") {
		cout << "-- (c)luster (dup)licate --" << endl;
		cout << "clusters file(s) by size into multiple group(s)." << endl;
		cout << endl;
		cout << "nc-mate cdup --help" << endl;
		exit(0);
	}
	if ((string) argv[1] == "--help") {
		cout << "-- (c)luster (dup)licate --" << endl;
		cout << "clusters file(s) by size into multiple group(s)." << endl;
		cout << endl;
		cout << "[PATTERN] nc-mate cdup <dir>" << endl;
		cout <<
		"clusters file(s) within <dir>ectory into multiple folder(s) of the same" <<
		" size."
		<< endl;
		exit(0);
	}
	if ((string) argv[1] == "--sim") {sim_cdup(argv[2]); exit(0);}
	proc_cdup(argv[1]);
}
