from sympy import *
x, y, a, b, u, v = symbols('x y a b u v')

eq1 = (x*y*(a**2-b**2)+a*b*(y**2-x**2)+a*y)
eq2 = (x**4-2*x**2+2*x**2*y**2+y**4+2*y**2+1)

eq3 = (x**2*(a**2-b**2)+y**2*(b**2-a**2)+4*a*b*x*y-(a**2+b**2))
eq4 = ((x**4)-(2*x**2)+2*x**2*y**2+y**4+2*y**2+1)

print solve([Eq(eq1 / eq2, u*v),Eq(eq3 / eq4, u**2-v**2)],[x, y])
