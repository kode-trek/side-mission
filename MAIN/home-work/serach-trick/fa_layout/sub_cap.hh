#include "rep_a.hh"

string sub(string arg1) {
 /* variable(s)
 [v1] gibberish-text
 */
 string v1 = arg1;
 // op(s)
 replace_a(v1, "‍!", "1");
 replace_a(v1, "٬", "2");
 replace_a(v1, "٫", "3");
 replace_a(v1, "﷼", "4");
 replace_a(v1, "٪", "5");
 replace_a(v1, "×", "6");
 replace_a(v1, "،", "7");
 replace_a(v1, "*", "8");
 replace_a(v1, ")", "9");
 replace_a(v1, "(", "0");
 replace_a(v1, "ـ", "q");
 replace_a(v1, "+", "w");
 replace_a(v1, "ْ", "e");
 replace_a(v1, "ٌ", "r");
 replace_a(v1, "ٍ", "t");
 replace_a(v1, "ً", "y");
 replace_a(v1, "ُ", "u");
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
