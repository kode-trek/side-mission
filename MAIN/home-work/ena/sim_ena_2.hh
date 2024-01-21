void sim_ena(string arg1, string arg2, string arg3) {
 /* variable(s)
 [v1] directory-name
 [v2] <n>-number-of-item(s)-in-[v1]
 [v3] <N>-initial-of-file-name(s)
 [v4] <ini>-initial-of-file-name(s)
 [v5] list-of-item(s)-in-[v1]
 [v6] temporary-directory-name-in-[v1]
 [cmd] color-command
 */
 string cmd = color("blue", "[] ");
 //
 if (arg1 == "") arg1 = pwd();
 string v1 = arg1 + "/";
 abbr(v1);
 //
 int v2 = 0;
 //
 int v3 = 0;
 if (arg2 == "") v3 = 1;
 else v3 = str2num(arg2);
 //
 string v4 = "";
 if (arg3 == "") v4 = "_";
 else v4 = arg3;
 //
 vector<string> v5 = {};
 string v6 = "." + ts();
 // op(s)
 if (not dir(v1)) {
  v2 = 1;
  v3 = 0;
 }
 if (dir(v1)) {
  cd(v1);
  v5 = tree(pwd(), false);
  v2 = v3;
  for(int i = 0; i < v5.size(); i++) {
   if (dir(v5[i])) continue;
   else (v2)++;
  }
 }
 cout <<
 cmd + "creates " + quote(v6) + " directory inside " + quote(v1) + ".""\n" +
 cmd + "moves file(s) within " + quote(v1) + " to " + quote(v6) + ".""\n" +
 cmd + "enumerates them: " + str(v3) + "~" + str(v2 - 1) + ".""\n" +
 cmd + "replaces them back to " + shortq(v1) + ".""\n" +
 cmd + "removes " + quote(v6) + "."
 << endl;
}
