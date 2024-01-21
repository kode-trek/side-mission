#include "proc_ena.hpp"
#include "sim_ena.hpp"

int main(int argc, char* argv[]) {
	if (str(argv[1]) == "") {
		cout <<
		"-- E N umerate A ll --""\n"
		"enumerates file(s) from N to (N + n).""\n"
		"\n"
		"nc-mate ena --help"
		<< endl;
		exit(0);
	}
	if (str(argv[1]) == "--help") {
		cout <<
		"-- E N umerate A ll --""\n"
		"enumerates file(s) from N to (N + n).""\n"
		"\n"
		"[PATTERN] nc-mate ena <dir> [N = 1]""\n"
		"renames all files of <dir> starting from N."
		<< endl;
		exit(0);
	}
	if (str(argv[1]) == "--sim") {sim_ena(argv[2], argv[3]); exit(0);}
	proc_ena(argv[1], argv[2]);
}
