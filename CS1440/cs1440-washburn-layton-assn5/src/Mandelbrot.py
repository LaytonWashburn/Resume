def mandelbrotIterationCounter(complexNumber, maxIterations): 	    	       
    """Return the iteration count for the Mandelbrot set"""  	    	 	      
    newComplex = complex(0, 0)     	       
    for iter in range(maxIterations):     	       
        newComplex = newComplex * newComplex + complexNumber   	    	       	    	       
        if abs(newComplex) > 2:  	    	       
            newComplex = float(2)  	    	         	    	         	    	       
            return iter
    return maxIterations - 1
            
              	  
    
 	    	       
