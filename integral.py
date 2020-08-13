import numpy as np

def f(x):
    return x**3+x**2+5

def rectangle(N,a,b):
    #Calculate the integral of a function using the rectangle rule. 
    
    #Inputs: num of bins (N)
    #Integration limits (a,b)
    #Returns: result of integral
    
    h = (b-a)/N
    s=0

    # Perform the integration
    for k in range(N):
        s += f(a+k*h)
    return h*s


print("Using the Riemann Summation of the midpoint method of intergration the total is: ", rectangle(1000,1,7))


def trapezoid(N,a,b):
    
    #Calculate the integral of a function using the trapezoidal rule.

    #Inputs: num of bins (N)
    #Integration limits (a,b)
    #Returns: result of integral

    h = (b-a)/N
    s = 0.5 * (f(a) + f(b))

    # Perform the integration
    for k in range(1,N):
        s += f(a + k*h)

    return h*s

print("Using the trapizoidal Riemann Summation method of integration the total is", trapezoid(1000,1,7))
