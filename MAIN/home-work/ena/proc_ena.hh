/*
 The MIT License (MIT)
 Copyright (c) 2023 Emeer Adhamian (github.com/kode-trek)
 https://raw.githubusercontent.com/kode-trek/mede/main/LICENSE
*/

#include "proc_ena_pt1.hh"
#include "proc_ena_pt2.hh"
#include "proc_ena_pt3.hh"
#include "proc_ena_pt4.hh"

void proc_ena(string arg1, string arg2, string arg3, string arg4) {
 /* variable(s)
 [v1] operation
 */
 string v1 = arg1;
 // op(s)
 if (v1 == "--enum") f1();
 if (v1 == "--replace") f2();
 if (v1 == "--remove") f2();
 if (v1 == "--add") f2();
}
