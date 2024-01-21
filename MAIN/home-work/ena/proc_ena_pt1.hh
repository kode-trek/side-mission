/*
 The MIT License (MIT)
 Copyright (c) 2023 Emeer Adhamian (github.com/kode-trek)
 https://raw.githubusercontent.com/kode-trek/mede/main/LICENSE
*/

void f1(string arg1, string arg2, string arg3) {}
// /* variable(s)
// [v1] directory-name
// [v2] <n>umber of item(s) in [v1]
// [v3] initial <N>umber of file-name(s)
// [v4] <initial> of file-name(s)
// [v5] list of item(s) in [v1]
// [v6] temporary folder-name in [v1]
// [v7] source
// [v8] target
// */
// string inp1 = mark("[inp] ", "blue");
// string out2 = mark("[out] ", "blue");
// string out1 = mark("[OK] ", "green");
// string err1 = mark("[WARNING] ", "yellow");
// //
// string v1 = can(arg1) + "/";
// int v2 = 0;
// int v3 = 0;
// if (arg2 == "") v3 = 1;
// if (arg2 != "") v3 = str2num(arg2);
// string v4 = "";
// if (arg3 == "") v4 = "_";
// if (arg3 != "") v4 = arg3;
// vector<string> v5 = {};
// string v6 = "." + ts();
// string v7, v8 = "";
// // op(s)
// if (not dir(v1)) {
//  cout <<
//  inp1 + v1 + "\n" +
//  err1 + "directory not found."
//  << endl;
//  exit(0);
// }
// cd(v1);
// if (not write_access()) {
//  cout <<
//  out2 + pwd() + "\n" +
//  err1 + "write-permission denied!"
//  << endl;
// }
// v5 = tree(pwd(), false);
// md(v6);
// v2 = v3;
// for(int i = 0; i < v5.size(); i++) {
//  if (dir(v5[i])) continue;
//  if (not dir(v5[i])) {
//   v7 = v5[i];
//   v8 = v6 + "/" + v4 + str(v2) + uri(v7, "extension");
//   mv(v7, v8);
//   (v2)++;
//  }
// }
// v5 = tree(v6);
// for(int i = 0; i < v5.size(); i++) {
//  v7 = v5[i];
//  v8 = pwd();
//  mv(v7, v8);
// }
// rm(v6);
// cout << out1 + "file(s) renamed: " + str(v3) + "~" + str(v2 - 1) << endl;
//}
