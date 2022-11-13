def phoenixIterationCounter(complexNumber, maxIterations):  	    	       
    """  	    	       
    Returns an iteration
    """  	    	             
    juliaConstant = complex(0.5667, 0.0)  	    	       	       
    pheonixConstant = complex(-0.5, 0.0)  	    	              
    compflipped = complex(complexNumber.imag, complexNumber.real)  	    	       
    prevComplex = 0+0j  	    	        	    	       	    	       
    for iter in range(maxIterations):	    	       
        savedComplex = compflipped     	             
        compflipped = compflipped * compflipped + juliaConstant + (pheonixConstant * prevComplex)  	  	       
        prevComplex = savedComplex   	    	       
        if abs(compflipped) > 2:  	    	       
            return iter     	            	              
    return maxIterations - 1           