import sympy as sp
def ConcaveUp(expr_input,lower,upper):
    x = sp.symbols('x')

    expr = sp.sympify(expr_input)

    der = sp.diff(expr)
    double_der = sp.diff(der)

    i = lower
    inflection_points = []

    while i <= upper:
        if -0.01 < double_der.evalf(subs={x:i}) < 0.01:
            inflection_points.append(i)
            i = i + 0.001
            
        else:
            i = i + 0.001
            
    i = 0

    while i <=len(inflection_points) - 2:
        if -0.02 < inflection_points[i] - inflection_points[i+1] <= 0.02:
            del inflection_points[i]
            
        else:
            i = i + 1    
    points = []

    i = 0

    while i<= len(inflection_points) - 1:
        points.append(inflection_points[i])
        i = i + 1
        
    points.insert(0, lower)
    points.append(upper)

    i = 0

    while i <=len(points) - 2:
        if -0.02 < points[i] - points[i+1] <= 0.02:
            del points[i]
            
        else:
            i = i + 1
            
    #print(points)


    concavity_middle_points = []

    i = 0

    while i <= len(points)-2:
        middle_point = (points[i] + points[i+1]) / 2
        
        if double_der.evalf(subs={x:middle_point}) > 0:
            concavity_middle_points.append(1)
            
        elif double_der.evalf(subs={x:middle_point}) < 0:
            concavity_middle_points.append(0)
            
        i = i + 1
        
    #print(concavity_middle_points)
        
    concave_up = []
    interval = ''
    i = 0
    while i <= len(concavity_middle_points) - 1:
        if concavity_middle_points[i] == 1:
            interval = '(' + str(round(points[i],3)) + ',' + str(round(points[i+1],3)) + ')'
            concave_up.append(interval)        
        i = i + 1
    return concave_up   
        
def ConcaveDown(expr_input,lower,upper):
    x = sp.symbols('x')
    expr = sp.sympify(expr_input)
    der = sp.diff(expr)
    double_der = sp.diff(der)
    i = lower
    inflection_points = []

    while i <= upper:
        if -0.01 < double_der.evalf(subs={x:i}) < 0.01:
            inflection_points.append(i)
            i = i + 0.001
            
        else:
            i = i + 0.001
    i = 0

    while i <=len(inflection_points) - 2:
        if -0.02 < inflection_points[i] - inflection_points[i+1] <= 0.02:
            del inflection_points[i]    
        else:
            i = i + 1    
    #print(inflection_points)
    points = []
    i = 0
    while i<= len(inflection_points) - 1:
        points.append(inflection_points[i])
        i = i + 1    
    points.insert(0, lower)
    points.append(upper)
    i = 0
    while i <=len(points) - 2:
        if -0.02 < points[i] - points[i+1] <= 0.02:
            del points[i]
            
        else:
            i = i + 1
    concavity_middle_points = []

    i = 0

    while i <= len(points)-2:
        middle_point = (points[i] + points[i+1]) / 2
        
        if double_der.evalf(subs={x:middle_point}) > 0:
            concavity_middle_points.append(1)
            
        elif double_der.evalf(subs={x:middle_point}) < 0:
            concavity_middle_points.append(0)
            
        i = i + 1

    concave_down = []

    interval = ''
    i = 0

    while i <= len(concavity_middle_points) - 1:
        if concavity_middle_points[i] == 0:
            interval = '(' + str(round(points[i],3)) + ',' + str(round(points[i+1],3)) + ')'
            concave_down.append(interval)
            
        i = i + 1    
        
    return concave_down   

