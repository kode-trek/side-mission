int main() {
 //var(s)
 string v1 = "";
 int v2 = 0;
 // op(s)
 for (int i = 1; i <= 32; i++) {
  v1 = str(i);
  for (int j = 0; j < v1.size(); j++) v2 += str2num(v1[j]);
  cout << v1 << "\t" << v2 << "\t";
  if ((v1 == "6") or (v1 == "28")) cout << "perfect-number" << endl;
  else cout << endl;
  v2 = 0;
 }
 k2c();
}
