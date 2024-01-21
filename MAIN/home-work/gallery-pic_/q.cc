bool dropls(string arg1, vector<string> arg2, string arg3="", string arg4="") {
 string v1 = can(arg1);
 vector<string> v2 = arg2;
 FILE *v3 = NULL;
 #ifdef __linux__
 v3 = fopen(v1.c_str(), "a");
 #endif
 #ifdef _WIN32
 v3 = _wfopen(u8(v1).c_str(), L"a,ccs=UTF-8");
 #endif
 if (not v3) return true;
 for (int i = 0; i < v2.size(); i++)
  fprintf(v3, "%s\n", u8(arg3 + v2[i] + arg4).c_str());
 fclose(v3);
 return false;
}

int main(int argc, char* argv[]) {
 if (argc < 2) {
  cout << "needs 1 argument." << endl;
  exit(0);
 }
 /* variable(s)
 [v1] input-directory
 [v2] list of file(s) in [v1]
 [v3] same [v2] with absolute-path excluded (only file-name(s)).
 [v4] temparory file-name
 */
 string inp1 = mark("[inp] ", "blue");
 string err1 = mark("[err] ", "red");
 //
 string v1 = argv[1];
 v1 = can(v1);
 vector<string> v2 = {};
 vector<string> v3 = {};
 string v4 = ts();
 // message(s)
 string msg1 =
 inp1 + v1 + "\n" +
 err1 + "directory not found.";
 // op(s)
 if (not dir(v1)) {
  cout << msg1 << endl;
  exit(0);
 }
 v2 = tree(v1);
 for (int i = 0; i < v2.size(); i++)
  v3.push_back(uri(v2[i], "full-name"));
 cout << drop("img_DB.js", "var img_ls = [""\n") << endl;
 dropls("img_DB.js", v3, "\"", "\",");
 drop("img_DB.js", "]");
// for (int i = 0; i < v2.size(); i++)
//  dropls(v4, uri(v2[i], "full-name"));
// vector<string> v3 = split(cat("a"), "\n");
// drop(ts(),
// "<script>""\n"
// "var img_list = [""\n"
//  
//var lst = [
//"1.jpg",
//"2.torrent",
//"3.jpg",
//]
//)
// string v1 = "";
// string v2 = "";
// vector<string> v3 = split(cat("a"), "\n");
// //
// for (int i = 0; i < v3.size(); i++) {
//  v2 = R"(<div class="mySlides fade"><img src=")" + v3[i] +
//  R"(" style="width:100%"></div>)";
//  cout << v2 << endl;
// }
}
