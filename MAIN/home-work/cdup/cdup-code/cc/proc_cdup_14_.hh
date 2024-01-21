void proc_cdup(string arg1=pwd()) {
 /* variable(s)
 [v1] directory
 [v2] list of file(s) in [v1] / later as unique-v[4]
 [v3] same list with folder(s) excluded
 [v4] size(s) of file(s) in [v3]
 [v5] temp-name
 */
 string inp1 = mark("[inp] ", "blue");
 string inp2 = mark("[pwd] ", "blue");
 string cmd = mark("[] ", "blue");
 string out1 = mark("DONE.", "green");
 string err1 = mark("[WARNING] ", "yellow");
 //
 string v1 = can(arg1) + "/";
 vector<string> v2 = {};
 vector<string> v3 = {};
 vector<int> v4 = {};
 string v5 = ts();
 // message(s)
 string msg1 = cmd + "clustering file(s)...";
 // op(s)
 if (not dir(v1)) {
  cout <<
  inp1 + v1 + "\n" +
  err1 + "directory not found."
  << endl;
  exit(0);
 }
 if (not write_access(v1)) {
  cout <<
  inp1 + v1 + "\n" +
  err1 + "write-permission denied."
  << endl;
  exit(0);
 }
 note(msg1);
 v2 = tree(v1, false);
 for (int i = 0; i < v2.size(); i++) {
  if (dir(v2[i])) continue;
  if (not dir(v2[i])) v3.push_back(v2[i]);
 }
 for (int i = 0; i < v3.size(); i++) {
  v4.push_back(space(v3[i]));
  md(v1 + "CLUST_" + str(space(v3[i])) + v5);
  mv(v3[i], v1 + "CLUST_" + str(space(v3[i])) + v5);
 }
 v2 = unique(str(v4));
 // eliminates clusters with only 1 item
 for(int i = 0; i < v2.size(); i++) {
  if (tree(v1 + "CLUST_" + v2[i] + v5, false).size() == 1) {
   mv(tree(v1 + "CLUST_" + v2[i] + v5, false)[0], v1);
   rm(v1 + "CLUST_" + v2[i] + v5);
  }
 }
 cout << out1 << endl;
}
