def Vertical(expr_input,lower,upper):
    import sympy as sp
    from sympy import oo
    x = sp.symbols('x')
    h = sp.symbols('h')
    expr = sp.sympify(expr_input)
    expr_h = expr.evalf(subs={x:h})
    #print(exp_h)

    diff = sp.diff(expr)
    diff_h = diff.evalf(subs={x:h})

    #print(diff_h)

    tangent = (diff_h)*x + expr_h - h*(diff_h)

    reciprocal = 1/(expr)

    discontinuity_points = []

    i = lower

    while i <= upper:
        
        if i == 0:
            i = i + 0.01
            
        if -0.02 <= reciprocal.evalf(subs={x:i}) <= 0.02:
            discontinuity_points.append(i)
            i = i + 0.01
            
        else:
            i = i + 0.01


    i = 0

    if len(discontinuity_points) != 1:
        while i <= len(discontinuity_points) - 2:
            if -0.02 <= discontinuity_points[i+1] - discontinuity_points[i] <= 0.02:
                del discontinuity_points[i]
                
            else:
                i = i + 1

    i = 0
    Vertical_asymptotes=[]
    while i <= len(discontinuity_points) - 1:
        Vertical_asymptotes.append(round(discontinuity_points[i],3))
        # print('No.', i + 1, 'vertical asymptote of the function is x =', round(discontinuity_points[i],3))
        
        i = i + 1
    
    return Vertical_asymptotes

# print(Vertical("tan(x)",-10,10))  