import sympy as sp
def limit(str_expression,limitingPoint):
    x = sp.symbols('x')
    # str_expression = input("Enter a function : ")
    # limitingPoint = int(input("Enter the limiting point: "))
    expression = sp.sympify(str_expression)
    # print("Expression : {}".format(expression))
	
    # Use sympy.limit() method
    lhl = sp.limit(expression, x,  int(limitingPoint),dir="-")
    rhl = sp.limit(expression, x,  int(limitingPoint),dir="+")
    
    if lhl==rhl:
        return lhl
    else:
        return "DNE"
    
	

