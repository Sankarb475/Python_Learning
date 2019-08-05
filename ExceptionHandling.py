Exceptions are unexpected events that occur during the execution of a program. 
Exceptions (also known as errors) are objects that are raised (or thrown) by code that encounters an unexpected circumstance.
A raised error may be caught by a surrounding context that “handles” the exception in an appropriate fashion. If uncaught, an exception causes 
the interpreter to stop executing the program and to report an appropriate message to the console.

TypeError Raised when wrong type of parameter is sent to a function ==> abs('hello')
ValueError Raised when parameter has invalid value (e.g., sqrt(−5))

#Raising an exception ::
we can raise an exception using the keyword "raise"

def sqrt(x):
    x = 'Sankar'
    if not isinstance(x, (int, float)):
        raise TypeError( "x must be numeric")
    elif x < 0:
        raise ValueError( "x cannot be negative" )
        
 
try:
    fp = open( sample.txt )
except IOError as e:
    print( Unable to open the file: , e)
    
#Two types of error being handled at a time ::
except (ValueError, EOFError):
  print("Invalid response")
  
except ValueError:
  print( That is an invalid age specification )
except EOFError:
  print( There was an unexpected error reading input. )
  raise # lets re-raise this exception
