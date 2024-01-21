int main(int argc, char* argv[]) {
 if (argc < 2) {
  cout << "needs 1 argument." << endl;
  exit(0);
 }
 string v1 = argv[1];
 vector<string> v2 = split(v1, " ");
 string v3 = "";
 for (int i = 0; i < v2.size(); i++) v3 += v2[i] + "+";
 cout << R"(https://www.google.com/search?q=related:)" + v3.substr(0, v3.size() - 1) << endl;
}
