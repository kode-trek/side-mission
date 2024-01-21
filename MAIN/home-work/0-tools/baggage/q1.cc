int main (int argc, char* argv[]) {
 if (argc < 3) {
  cout << "needs 2 arg(s)." << endl;
  exit(0);
 }
 string v1 = argv[1];
 string v2 = argv[2];
 vector<string> v3 = tree(v1);
 vector<string> v4 = tree(v2);
 int e = 1;
 string cmd1 = "";
 //
 seedr();
 for (int i = 0; i < v4.size(); i++) {
  if (dir(v4[i])) continue;
  if (not exist(v1 + "/" + uri(v4[i], "full-name"))) {
   mv(v4[i], v1);
   continue;
  }
  cmd1 = "diff " + quote(v4[i]) + " " + quote(v1 + "/" +
  uri(v4[i], "full-name"));
  e = sys(cmd1);
  if (not e) rm(v4[i]);
  if (e) mv(v4[i], v1 + "/" + uri(v4[i], "full-name") + "_" + str(rand()));
 }
}
