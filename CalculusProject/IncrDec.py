def Increasing(expr_input,lower,upper):
    import sympy as sp
    x = sp.symbols('x')
    expr = sp.sympify(expr_input)

    diff = sp.diff(expr)
    #print(diff)

    der = sp.solve(diff)
 

    #now checking if extrema lies in the interval

    check = []

    #check contains all x coordinates of extremas lying in the interval given by the user

    i = 0

    while i <= len(der)-1:
        if lower < der[i] < upper :
            check.append(der[i])
            i = i + 1
            
        else:
            i = i + 1
            
    check.sort()
    points = check
    points.insert(0, lower)
    points.append(upper)
    #points contain x coordinates of important points (lower, extremas, and upper)
            
    value_lower = expr.evalf(subs={x:lower})
    value_upper = expr.evalf(subs={x:upper})

    values_extrema = []

    i = 0

    while i <= len(check)-1:
        values_extrema.append(expr.evalf(subs={x:check[i]}))
        i = i + 1
    values_point = values_extrema
    values_point.insert(0,value_lower)
    values_point.append(value_upper)
    #values point has the values at all the important points (starting, extremas, and ending)

    comparision = []

    i = 0

    while i <= len(values_point)-2:
        if values_point[i] < values_point[i+1]:
            comparision.append(1)
              
        if values_point[i] > values_point[i+1]:
            comparision.append(0)
            
        i = i + 1

    i = 0
    increasing = []
    interval = ''
    while i<= len(comparision)-1:
        if comparision[i] == 1:
            interval = '(' + str(points[i]) + ',' + str(points[i+1]) + ')'
            increasing.append(interval)   
        i = i + 1    
    return increasing


def Decreasing(expr_input,lower,upper):
    import sympy as sp
    x = sp.symbols('x')
    expr = sp.sympify(expr_input)

    diff = sp.diff(expr)
    #print(diff)

    der = sp.solve(diff)

    check = []
    i = 0

    while i <= len(der)-1:
        if lower < der[i] < upper :
            check.append(der[i])
            i = i + 1
            
        else:
            i = i + 1
            
    check.sort()
    #print(check)
    points = check
    points.insert(0, lower)
    points.append(upper)
    #points contain x coordinates of important points (lower, extremas, and upper)
            
    value_lower = expr.evalf(subs={x:lower})
    value_upper = expr.evalf(subs={x:upper})

    values_extrema = []

    i = 0

    while i <= len(check)-1:
        values_extrema.append(expr.evalf(subs={x:check[i]}))
        i = i + 1
        
    values_point = values_extrema
    values_point.insert(0,value_lower)
    values_point.append(value_upper)
    comparision = []

    i = 0

    while i <= len(values_point)-2:
        if values_point[i] < values_point[i+1]:
            comparision.append(1)
            
            
        if values_point[i] > values_point[i+1]:
            comparision.append(0)
            
        i = i + 1

    i = 0
    decreasing = []
    interval = ''

    while i<= len(comparision)-1: 
        if comparision[i] == 0:
            interval = '(' + str(points[i]) + ',' + str(points[i+1]) + ')'
            decreasing.append(interval)
            
        i = i + 1
        
    return decreasing

