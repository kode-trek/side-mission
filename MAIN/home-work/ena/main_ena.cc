/*
 The MIT License (MIT)
 Copyright (c) 2023 Emeer Adhamian (github.com/kode-trek)
 https://raw.githubusercontent.com/kode-trek/mede/main/LICENSE
*/

#include "proc_ena.hh"
#include "sim_ena.hh"

int main(int argc, char* argv[]) {
 /* variable(s) */
 string v1 = mark("-- ENumerate All --", "blue");
 string v2 = mark("--help", "blue");
 string v3 = mark("[PATTERN] ", "blue");
 // op(s)
 if (str(argv[1]) == "") {
  cout <<
  v1 + "\n"
  "renames/enumerates file(s) from N to (N + n).""\n"
  "mede ena " + v2
  << endl;
  exit(0);
 }
 if (str(argv[1]) == "--help") {
  cout <<
  v3 + "mede ena <dir> [<N>=1] [<initial>=_]""\n"
  "renames all file(s) in <dir>ectory initiating with <_N>."
  << endl;
  exit(0);
 }
 if (str(argv[1]) == "SIM") {
  sim_ena(argv[2], argv[3], argv[4], argv[5]);
  exit(0);
 }
 proc_ena(argv[1], argv[2], argv[3], argv[4]);
}
