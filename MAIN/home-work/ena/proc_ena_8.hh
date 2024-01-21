void proc_ena(string arg1, string arg2, string arg3) {
 /* variable(s)
 [v1] directory-name
 [v2] <n>umber-of-item(s)-in-[v1]
 [v3] initial-<N>umber-of-file-name(s)
 [v4] <initial>-of-file-name(s)
 [v5] list-of-item(s)-in-[v1]
 [v6] temporary-directory-name-in-[v1]
 [v7] source
 [v8] target
 [inp] color-input
 [cmd] color-command
 [out] color-output
 [err] color-error/warning
 */
 string inp1 = color("blue", "[inp] ");
 string inp2 = color("blue", "[pwd] ");
 string out1 = color("green", "[OK] ");
 string err1 = color("yellow", "[WARNING] ");
 //
 string v1 = arg1 + "/";
 abbr(v1);
 int v2 = 0;
 int v3 = 0;
 if (arg2 == "") v3 = 1;
 else v3 = str2num(arg2);
 string v4 = "";
 if (arg3 == "") v4 = "_";
 else v4 = arg3;
 vector<string> v5 = {};
 string v6 = "." + ts();
 string v7, v8 = "";
 // op(s)
 if (not dir(v1)) {
  cout <<
  inp1 + v1 + "\n" +
  err1 + "directory not found."
  << endl;
  exit(0);
 }
 if (not write_access()) {
  cout <<
  inp2 + pwd() + "\n" +
  err1 + "write-permission denied!"
  << endl;
  exit(1);
 }
 cd(v1);
 v5 = tree(pwd(), false);
 md(v6);
 v2 = v3;
 for(int i = 0; i < v5.size(); i++) {
  if (dir(v5[i])) continue;
  else {
   v7 = v5[i];
   v8 = v6 + "/" + v4 + str(v2) + uri(v5[i])[3];
   mv(v7, v8);
   (v2)++;
  }
 }
 v5 = tree(v6);
 for(int i = 0; i < v5.size(); i++) {
  v7 = v5[i];
  v8 = pwd();
  mv(v7, v8);
 }
 rm(v6);
 cout << out1 + "file(s) renamed: " + str(v3) + "~" + str(v2 - 1) << endl;
}
