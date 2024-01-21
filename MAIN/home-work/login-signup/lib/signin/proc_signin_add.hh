/*
 The MIT License (MIT)
 Copyright (c) 2023 Emeer Adhamian (github.com/kode-trek)
 https://raw.githubusercontent.com/kode-trek/who/main/LICENSE
*/

void _add(string arg1, string arg2, string arg3) {
 /* variable(s)
 [v1] option
 [v2] ID
 [v3] sub-option
 [v4] item
 [v5] record-name
 */
 string inp1 = mark("blue", "[name] ");
 string inp2 = mark("blue", "[link] ");
 string inp3 = mark("blue", "[docx] ");
 string cmd = mark("blue", "[] ");
 string out1 = mark("blue", "[out] ");
 string out2 = mark("green", "DONE.");
 string err1 = mark("red", "HALTED.""\n""[FAILED] ");
 //
 string v1 = arg1;
 string v2 = arg2;
 string v3 = arg3;
 string v4 = arg4;
 can(v4);
 string v5 = "~/who-DB/" + ts();
 can(v5);
 // message(s)
 string msg1 = "creating new slot...";
 string msg2 = "";
 if (v3 == "-name") {
  msg2 =
  inp1 + v4 + "\n" +
  out1 + v5 + "/INFO.txt""\n" +
  cmd + "adding item to record...";
 }
 if (v3 == "-link") {
  msg2 =
  inp2 + v4 + "\n" +
  out1 + v5 + "/INFO.txt""\n" +
  cmd + "adding item to record...";
 }
 if (v3 == "-docx") {
  msg2 =
  inp3 + uri(v4)[1] + "\n" +
  out1 + v5 + "\n" +
  cmd + "adding item to record...";
 }
 // command(s)
 int e = 0;
 // op(s)
 if (v1 == "--new") {
  note(msg1);
  e = md(v5);
  if (e) {
   cout << err1 + "cannot access directory." << endl;
   exit(1);
  }
 }
 if ((v1 == "--id") and (v3 == "-name")) {
  note(msg2);
  e = drop("~/who-DB/" + v2 + ".txt", "NAME=" + v4 + "\n");
  if (e) {
   cout << err1 + "cannot access file." << endl;
   exit(1);
  }
 }
 if ((v1 == "--id") and (v3 == "-link")) {
  note(msg2);
  e = drop("~/who-DB/" + v2 + ".txt", "LINK=" + v4 + "\n");
  if (e) {
   cout << err1 + "cannot access file." << endl;
   exit(1);
  }
 }
 if ((v1 == "--id") and (v3 == "-docx")) {
  note(msg2);
  e = cp("~/who-DB/" + v2, v4);
  if (e) {
   cout << err1 + "cannot access directory." << endl;
   exit(1);
  }
 }
}
