i686-w64-mingw32-gcc src.c
mv a.exe setup.exe
mkisofs -o my_cd.iso autorun.inf setup.exe
