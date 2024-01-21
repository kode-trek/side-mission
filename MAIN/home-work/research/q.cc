/*
 The MIT License (MIT)
 Copyright (c) 2023 Emeer Adhamian (github.com/kode-trek)
 https://raw.githubusercontent.com/kode-trek/side-quest/main/LICENSE
*/
int main(int argc, char* argv[]) {
 /* variable(s)
 [v1] entry
 [v2] search-item-vector
 [v3] search-item-string
 [v4] html-code
 [v5] output-htm-file
 */
 string cmd = mark("[] ", "blue");
 string out1 = mark("[out] ", "blue");
 string out2 = mark("DONE.", "blue");
 //
 if (argc < 2) {
  cout << "needs 1 argument." << endl;
  exit(0);
 }
 string v1 = argv[1];
 vector<string> v2 = {};
 string v3 = "";
 string v4 = "";
 string v5 = ts() + ".htm";
 // message(s)
 string msg1 = cmd + "building HTML-page...";
 string msg2 = out1 + v5;
 // op(s)
 v2 = split(v1, " ");
 for (int i = 0; i < v2.size(); i++) v3 += v2[i] + "+";
 v3 = v3.substr(0, v3.size() - 1);
 v4 = R"(
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <p>[ITEM] <span>)" + v1 + R"(</span></p>
 <hr>
 <a href="https://www.refseek.com/search?q=)" + v3 + R"(">refseek.com</a>
 <br>
 <a href="https://www.worldcat.org/search?q=)" + v3 + R"(">worldcat.org</a>
 <br>
 <a href="https://link.springer.com/search?query=)" + v3 +
 R"(">link.springer.com</a>
 <br>
 <a href="http://bioline.org.br/search?search_target=all_pub&search_string=)" +
 v3 + R"(">bioline.org.br</a>
 <br>
 <a href="http://repec.org/">repec.org</a>
 <br>
 <a href="https://www.science.gov/">science.gov</a>
 <br>
 <a href="http://www.pdfdrive.com/search?q=)" + v3 + R"(">pdfdrive.com</a>
 <br>
 <a href="https://www.base-search.net/Search/Results?lookfor=)" + v3 +
 R"(">base-search.net</a>
 )";
 note(msg1);
 drop(v5, v4);
 cout << out2 + "\n" + msg2 << endl;
}
