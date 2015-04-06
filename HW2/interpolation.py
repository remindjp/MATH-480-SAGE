"""
Jingpeng Wu Math 480 HW#2 
"""

import numpy
from numpy.linalg import solve

def interpolation(xi,yi):
    """
    Given numpy arrays xi, yi that have the x,y (float) coordinates of the ith point respectively,
    prints an (i-1)th degree polynomial that satisfies those points

    """

    # Set up linear system to interpolate through data points:
    length = len(xi)
    arguments = []
    xs = [1]
    arguments.append(numpy.ones(length))
      
    for x in range(1,length):
        arguments.append(xi**x)
        xs.append("x^" + str(x))
    
    # Ax = B   
    A = numpy.vstack(tuple(arguments)).T
    B = yi      
    x = solve(A,B)
    
    #simple printing

    print "x coordinates: " + str(xi)
    print "y coordinates: " + str(yi)
    
    print "function:",
    for i in range(length - 1, 0, -1):
        if x[i] > 0.0:    
            print str("%.2f" % x[i]) + str(xs[i]) + " +",       
    
    if x[0] > 0:           
        print str("%.2f" % x[0]) + str(xs[0]),
    else:
        print 0.000
        

def test():
    xi =numpy.array([-1., 0., 1.])
    yi =numpy.array([1., 0., 1.])
    interpolation(xi,yi)  
    
if __name__=="__main__":
    test()
    
  
