#include "proc_cdup.hh"

int main(int argc, char* argv[]) {
 // var(s)
 string v1 = mark("-- Cluster DUPlicate(s) --", "blue");
 string v2 = mark("--help", "blue");
 string v3 = mark("[PATTERN] ", "blue");
 // op(s)
 if (str(argv[1]) == "") {
  cout <<
  v1 << "\n"
  "re-arranges file(s) into several cluster(s).""\n"
  "cdup " << v2
  << endl;
  exit(0);
 }
 if (str(argv[1]) == "--help") {
  cout <<
  v3 << "cdup <dir>""\n"
  "clusters file(s) of <dir>ectory into multiple folder(s) based on their "
  "common features, such as file-type and size."
  << endl;
  exit(0);
 }
 proc_cdup(argv[1]);
}
