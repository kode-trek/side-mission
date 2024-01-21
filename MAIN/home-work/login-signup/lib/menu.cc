/*
 The MIT License (MIT)
 Copyright (c) 2023 Emeer Adhamian (github.com/kode-trek)
 https://raw.githubusercontent.com/kode-trek/who/main/LICENSE
*/

int main() {
 /* variable(s)
 [v1] key-value
 */
 map<string, string> v1;
 v1["sign-up"] = "\t""\t""creats account.";
 v1["sign-in"] = "\t""\t""proceeds as signed-in user.";
 // op(s)
 for (auto item : v1)
  cout << "[" + mark(item.first, "blue") + "] " + item.second << endl;
}
