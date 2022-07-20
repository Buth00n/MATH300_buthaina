
from sympy import diff, cos, exp, pi
from sympy.abc import x
expr = (x**3) - (cos((pi**2)*(x**2))/(2*(x**2)+1)) + (11/3*x**2) - 1
diff(expr, x)
print(diff(expr, x))