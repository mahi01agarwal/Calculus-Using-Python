import DerivativeOfFunction
import Limit
import CriticalPoints
import sympy as sp


def FindMaxima(function):
    maxima =[]
    x = sp.Symbol('x')
    derivative = DerivativeOfFunction.derivative(function)
    doublederivative = DerivativeOfFunction.derivative(derivative)
    criticalPoints = CriticalPoints.criticalPoints(function)
    for i in range(0,len(criticalPoints)):
        ans = Limit.limit(doublederivative,criticalPoints[i])
        if ans<0:
            maxima.append(criticalPoints[i])
    return maxima

def FindMinima(function):
    minima =[]
    x = sp.Symbol('x')
    derivative = DerivativeOfFunction.derivative(function)
    doublederivative = DerivativeOfFunction.derivative(derivative)
    criticalPoints = CriticalPoints.criticalPoints(function)
    for i in range(0,len(criticalPoints)):
        ans = Limit.limit(doublederivative,criticalPoints[i])
        if ans>0:
        
                minima.append(criticalPoints[i])
                
    return minima
             
                            
        
    





