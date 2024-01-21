/*
 The MIT License (MIT)
 Copyright (c) 2023 Emeer Adhamian (github.com/kode-trek)
 https://raw.githubusercontent.com/kode-trek/who/main/LICENSE
*/

int main() {
 string v1 = mark("-- WHO - Address Book--", "blue");
 string v2 = mark("[PATTERN] ", "blue");
 string v3 = mark("Linux Mint 21.1 (vera)", "yellow");
 // op(s)
 cout <<
 v1 + "\n" +
 "an address data-bank.""\n" +
 v2 + "mede cmd""\n"
 "enlists commands.""\n" +
 v2 + "mede <cmd> --help""\n"
 "displays manual for <cmd>.""\n""\n"
 "this terminal-app has been tested on " + v3 + " platform.""\n"
 "[development] github.com/kode-trek"
 << endl;
}
