def Asymptotes(expr_input):
    import sympy as sp
    from sympy import oo
    from sympy import Piecewise, Eq, pprint
    x = sp.symbols('x')
    h = sp.symbols('h')
    e = 2.71828
    f = Piecewise((0, Eq(x, 0)), (sp.tan(x), True))
    expr = sp.sympify(expr_input)
    expr_h = expr.evalf(subs={x:h})
    #print(exp_h)

    diff = sp.diff(expr)
    diff_h = diff.evalf(subs={x:h})

    #print(diff_h)

    tangent = (diff_h)*x + expr_h - h*(diff_h)


    asymptote1 = sp.limit(tangent, h, oo)
    asymptote2 = sp.limit(tangent, h, -oo)

    MyAsymptotes = []
    

    if asymptote1 != oo and asymptote1 != -oo:
        # print('Asymptote of the function is: y =', asymptote1)
        MyAsymptotes.append(asymptote1)
        # print(MyAsymptotes)

    if asymptote2 != oo and asymptote2 != -oo and asymptote2 != asymptote1:
        if asymptote1 != oo and asymptote1 != -oo:
            # print('Second asymptote of the function is: y =', asymptote2)
            MyAsymptotes.append(asymptote2)
            # print(MyAsymptotes)
            
        else:
            # print('Asymptote of the function is: y =', asymptote2)
            MyAsymptotes.append(asymptote2)
            # print(MyAsymptotes)
            
        # return MyAsymptotes
    return MyAsymptotes
    
# print(Asymptotes("1/x") )      
            
 