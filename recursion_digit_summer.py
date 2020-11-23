m'''question: given an integer, create a function that returns 
the sum of all the individual digits in that integer. 
example, n=4321, returns 4+3+2+1 or 10''' 

def digit_summer(n): 
    
   if int (n/10)==0:  
       return int(n%10)
   else:      
       return (int(n%10)+digit_summer(n/10))
       
print (digit_summer(4502))