import sympy 

def derivative(function):
    x = sympy.Symbol('x')
    log = sympy.Symbol('log')
    antilog = sympy.Symbol('antilog')

    # function = input("Enter a function: ")

    function = sympy.sympify(function)
    # print(function)

    derivative = sympy.diff(function, x)
    # print(derivative)
    return derivative


