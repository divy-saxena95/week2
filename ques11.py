def  evalQuadratic(a, b, c, x):
    """
    a,b,c,x:int or float
    
    """
    m=((a*(x**2))+(b*x)+c)
    return m

r=evalQuadratic (1, 2, 3, 4)
print "The result is " + str(r)