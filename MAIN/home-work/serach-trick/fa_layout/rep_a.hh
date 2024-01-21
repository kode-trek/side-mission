void replace_a(string& str, const string& from, const string& to) {
 if (from.empty()) return;
 size_t start_pos = 0;
 while ((start_pos = str.find(from, start_pos)) != string::npos) {
  str.replace(start_pos, from.length(), to);
  start_pos += to.length();
 }
}

bool replace(string& str, const string& from, const string& to) {
 size_t start_pos = str.find(from);
 if(start_pos == string::npos)
  return false;
 str.replace(start_pos, from.length(), to);
 return true;
}
