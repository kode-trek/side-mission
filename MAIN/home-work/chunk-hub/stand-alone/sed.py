import os

os.system("sed '1,1622166!d' stk.dat > dat1")
os.system("sed '1622166,3244332!d' stk.dat > dat2")
os.system("sed '3244332,4866498!d' stk.dat > dat3")
os.system("sed '4866498,6488664!d' stk.dat > dat4")

os.system("sed '6488664,6488666!d' stk.dat > dat5")
