Polynomial Interpolation

+    Given numpy arrays xi, yi that have the x,y (float) coordinates of the ith point respectively,
+    this ATTEMPTS to print an (i-1)th degree polynomial that satisfies those points
+     

Examples of interpolation(xi,yi) 
    xi =numpy.array([-1., 0., 1.])
    yi =numpy.array([1., 0., 1.])
 
Output:
	x coordinates: [-1.  0.  1.]
	y coordinates: [ 1.  0.  1.]
	function: 1.00x^2 + 0.0
	
...

    xi =numpy.array([1.,2.,3.,4.])
    yi =numpy.array([1.,2.,3.,4.])
	
	x coordinates: [ 1.  2.  3.  4.]
	y coordinates: [ 1.  2.  3.  4.]
	function: 1.00x^1 + 0.0
	
...

    xi =numpy.array([1,2,3,4,5,6,7])
    yi =numpy.array([1,4,9,16,25,36,49])
	
	x coordinates: [1 2 3 4 5 6 7]
	y coordinates: [ 1  4  9 16 25 36 49]
	function: 1.00x^2 + 0.0	
	
	
	
	