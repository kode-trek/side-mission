#include "rep_a.hh"

string sub(string arg1) {
 /* variable(s)
 [v1] gibberish-text
 */
 string v1 = arg1;
 // op(s)
 replace_a(v1, "‍۱", "1");
 replace_a(v1, "۲", "2");
 replace_a(v1, "۳", "3");
 replace_a(v1, "۴", "4");
 replace_a(v1, "۵", "5");
 replace_a(v1, "۶", "6");
 replace_a(v1, "۷", "7");
 replace_a(v1, "۸", "8");
 replace_a(v1, "۹", "9");
 replace_a(v1, "۰", "0");
 replace_a(v1, "ض", "q");
 replace_a(v1, "ص", "w");
 replace_a(v1, "ث", "e");
 replace_a(v1, "ق", "r");
 replace_a(v1, "ف", "t");
 replace_a(v1, "غ", "y");
 replace_a(v1, "ع", "u");
 replace_a(v1, "ه", "i");
 replace_a(v1, "خ", "o");
 replace_a(v1, "ح", "p");
 replace_a(v1, "ج", "[");
 replace_a(v1, "چ", "]");
 replace_a(v1, "ش", "a");
 replace_a(v1, "س", "s");
 replace_a(v1, "ی", "d");
 replace_a(v1, "ب", "f");
 replace_a(v1, "ل", "g");
 replace_a(v1, "ا", "h");
 replace_a(v1, "ت", "j");
 replace_a(v1, "ن", "k");
 replace_a(v1, "م", "l");
 replace_a(v1, "ک", ";");
 replace_a(v1, "گ", "'");
 replace_a(v1, "ظ", "z");
 replace_a(v1, "ط", "x");
 replace_a(v1, "ز", "c");
 replace_a(v1, "ر", "v");
 replace_a(v1, "ذ", "b");
 replace_a(v1, "د", "n");
 replace_a(v1, "پ", "m");
 replace_a(v1, "و", ",");
 return v1;
}
