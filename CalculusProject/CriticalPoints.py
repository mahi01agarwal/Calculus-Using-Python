import sympy as sp
import DerivativeOfFunction
def criticalPoints(function):
    x = sp.Symbol('x')
    my_derivative = DerivativeOfFunction.derivative(function)
    criticalPoints = sp.solve(my_derivative,x)
    return criticalPoints
    # print(criticalPoints)