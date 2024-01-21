int main() {
 /* variable(s)
 [v1] name
 [v2] counter
 */
 string v1 = "";
 int v2 = 0;
 // op(s)
 cout << "name: ";
 cin >> v1;
 v1 = lower(v1);
 for (int i = 0; i < v1.size(); i++) {
  if (
  (str(v1[i]) == "o") or
  (str(v1[i]) == "i") or
  (str(v1[i]) == "u") or
  (str(v1[i]) == "a") or
  (str(v1[i]) == "e")
  ) v2++;
 }
 if (v2 % 2 != 0) cout << "boy" << endl;
 if (v2 % 2 == 0) cout << "girl" << endl;
 k2c();
}
