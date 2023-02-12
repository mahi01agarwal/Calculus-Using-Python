import sympy as sp
def Plot(str_function):
    function = sp.sympify(str_function)
    sp.plotting.plot(function,ylim=(-80,80))