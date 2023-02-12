import DerivativeOfFunction
import sympy as sp
def FindDoubleDerivative(function):
    x = sp.Symbol('x')
    derivative = DerivativeOfFunction.derivative(function)
    doubleDerivative = DerivativeOfFunction.derivative(derivative)
    return doubleDerivative