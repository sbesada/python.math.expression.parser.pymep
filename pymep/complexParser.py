from .exception import CalculatorException
from .complex import Complex
import math
import re

def parse(fx):
    return eval(fx, 0)
    

# fx(xi) or f(x,y,z,...) where xi is a var dictionary 
def eval(fx, xi):
    fx = fx.strip().lower().replace(" ","")


    value = 0.0
    number = ""
    function = ""
    hasNumber = False
    hasFunction = False
    isImaginary = False
    
    i = 0
    
    while (i < len(fx)):
        character = fx[i]
        
        if character == '*':     
            if hasNumber == True and isImaginary == False:
                numb = number
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.mul(Complex(float(numb),0), eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            
            elif hasNumber == True and isImaginary == True:
                numb = number
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.mul(Complex(0, float(numb)),eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            elif hasFunction == True:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.mul(eval(function, xi), eval(new_fx, xi))
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.mul(value, eval(new_fx, xi))
                i = i + len(new_fx)
         
         
        elif character == '+':   
    
            if hasNumber == True and isImaginary == False:
                numb = number
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = Complex.add(Complex(float(numb), 0),eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            
            elif hasNumber == True and isImaginary == True:
                numb = number
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = Complex.add(Complex(0, float(numb)), eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""    
            elif hasFunction == True:
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = Complex.add(eval(function, xi), eval(new_fx, xi))               
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = Complex.add(value,eval(new_fx, xi))
                i = i + len(new_fx)
                
                   
        elif character == '-':   
    
            if hasNumber == True and isImaginary == False:
                numb = number
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = Complex.sub(Complex(float(numb), 0), eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            
            elif hasNumber == True and isImaginary == True:
                numb = number
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = Complex.sub(Complex(0, float(numb)), eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
                
            elif hasFunction == True:
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = Complex.sub(eval(function, xi), eval(new_fx, xi))
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = Complex.sub(value, eval(new_fx, xi))

                i = i + len(new_fx)
                
        elif character == '/':     
            
            if hasNumber == True and isImaginary == False:
                numb = number
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.div(Complex(float(numb), 0), eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
                
            elif hasNumber == True and isImaginary == True:
                numb = number
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.div(Complex(0, float(numb)), eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            
            elif hasFunction == True:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.div(eval(function, xi), eval(new_fx, xi))
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.div(value, eval(new_fx, xi))

                i = i + len(new_fx)
    
        elif character == '^':     
            
            if hasNumber == True and isImaginary == False:
                numb = number
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.rpow(eval(new_fx, xi), float(numb))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
                
            elif hasNumber == True and isImaginary == False:
                numb = number
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.pow(eval(new_fx, xi), Complex(0, float(numb)))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
                
            elif hasFunction == True:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.pow(eval(function, xi), eval(new_fx, xi))
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = Complex.pow(value, eval(new_fx, xi))     
                i = i + len(new_fx)
                
        elif character == '0' or character == '1' or character == '2' or character == '3' or character == '4' or character == '5' or character == '6' or character == '7' or character == '8' or character == '9':
            
            if hasFunction == True:
               function = function + character
               
            else:    
                hasNumber = True
                number = number + character
                if i == len(fx) - 1:
                    value = Complex(float(number), 0)
                    number = ""
                    hasNumber = False
                
        elif character == '.':
            if i == len(fx) - 1:
                raise CalculatorException("The function is not well-formed")
            
            if hasNumber == True and len(number) > 0:
                number = number + character
                 
        elif character == '(':
    
            if i == len(fx) - 1:
                raise CalculatorException("The function is not well-formed")
            
    
            new_fx = fx[i + 1:nextBracket(fx)]
            if hasFunction==True:
                if function == "sin":
                    value = eval(new_fx, xi).__sin__()                        
    
                elif function == "cos":
                    value = eval(new_fx, xi).__cos__()
                    
                elif function == "tan":
                    value = eval(new_fx, xi).__tan__()
                
                elif function == "sinh":
                    value = eval(new_fx, xi).__sinh__()
                
                elif function == "cosh":
                    value = eval(new_fx, xi).__cosh__()
    
                elif function == "tanh":
                    value = eval(new_fx, xi).__tanh__()
    
                elif function == "asin":
                    value = eval(new_fx, xi).__asin__()
                    
                elif function == "acos":
                    value = eval(new_fx, xi).__acos__()  
                                          
                elif function == "atan":
                    value = eval(new_fx, xi).__atan__()
                
                #log10    
                elif function == "log10":
                    value = eval(new_fx, xi).__log10__()
                
                #log
                elif function == "log":
                    value = eval(new_fx, xi).__log__()
                    
                elif function == "sqrt":                    
                    value = eval(new_fx, xi).__sqrt__()
                    
                #elif function == "cbrt":
                #    value = math.cbrt(float(eval(new_fx, xi)))
                    
                else:
                    raise CalculatorException("The function is not well-formed")
                
    
                hasFunction = False
                function = ""
    
            else:
                value = eval(new_fx, xi)  
                              
            i = i + len(new_fx) + 1
    
            
        elif character == ')':     
            raise CalculatorException(" '(' is not finished ")
    
        elif character == ' ':  
            j = 0
            
        elif character == 'i' or character == 'j':
             
            if hasFunction == False:
 
                if hasNumber == True:

                    value = Complex(0, float(number))
                    number = ""
                    isImaginary = True
                else:
                    value = Complex(0, 1)
                    isImaginary = True
                    
                    
            else:

                function = function + character
                hasFunction = True

                if i == len(fx) - 1:
                    
                    if function == "e":
                        value = Complex(math.e,0)
    
                    elif function == "pi":
                        value = Complex(math.pi,0) 
                    
                    else:
                        possibleValue = getValue(function, xi)
                        
                        if isinstance(possibleValue, str):
                            value = eval(possibleValue, xi)
                        else:
                            value = possibleValue

                   
        else:
            if isValidCharacter(character):
                function = function + character
                hasFunction = True
    
                if i == len(fx) - 1:
    
                    if function == "e":
                        value = Complex(math.e,0)
    
                    elif function == "pi":
                        value = Complex(math.pi,0) 
                    
                    else:
                        possibleValue = getValue(function, xi)
                        
                        if isinstance(possibleValue, str):
                            value = eval(possibleValue, xi)
                        else:
                            value = possibleValue                       
                                              
            else:
                raise CalculatorException("Invalid character")
           
    
        i += 1
    return value

def getValue(function, xi):
    
    value = 0
    if len(function) == 1:
                            
        if isinstance(xi, dict):
            
            if function.lower() in xi:
                value = xi[function.lower()]
            elif function.upper() in xi:
                value = xi[function.upper()]
            else:
                raise CalculatorException("function is not well defined")          
            
        elif isinstance(xi, int):
            value = Complex(xi,0)
        elif isinstance(xi, float):
            value = Complex(xi,0)
        elif isinstance(xi, Complex):
            value = xi
        elif isinstance(xi, complex):
            value = Complex(xi.real,xi.imag)
        elif isinstance(xi, str):
            value = eval(xi, xi)
        else:
            raise CalculatorException("function is not well defined")
        
    return value
        
    
def nextFunction( fx):
    
    fx = fx.strip()
    
    result = ""
    
    i = 0
    
    while (i < len(fx)):
        character = fx[i]
        
        if character == '+' or character == '-' or character == '*' or character == '/':
            i = len(fx)
            
        elif character == '^' or character == '.' or character == ' ':
            result += character
        
        elif character == '(':
                   
            new_fx = fx[i:nextBracket(fx)+1]
            result += new_fx
            i = (i +len(fx))-1

        elif character == ')':
            raise CalculatorException(" '(' is not finished ")
        
        else:
            if isValidNumericAndCharacter(character):
                result = result + character
            else:
                raise CalculatorException("Invalid character")
        i+=1
            
    return result

def nextMinusFunction(fx):
    
    fx = fx.strip()
    
    result = ""
        
    i = 0
    
    while (i < len(fx)):
   
        character = fx[i]
        
        if character == '+' or character == '-' :
            i = len(fx)
            
        elif character == '^' or character == '.' or character == ' ' or character == '*' or character == '/':
            result += character
        
        elif character == '(':
                   
            new_fx = fx[i:nextBracket(fx)+1]
            result += new_fx
            i = (i +len(fx))-1

        elif character == ')':
            raise CalculatorException(" '(' is not finished ")
        
        else:
            if isValidNumericAndCharacter(character):
                result = result + character
            else:
                raise CalculatorException("Invalid character")
        
        i+=1    
    return result



def isValidCharacter(character):
    
    regexCharacter = re.compile('[a-z]')
    result = False
    
    if regexCharacter.match(character):
        result = True
    else: 
        result = False
    
    return result

def isValidNumericAndCharacter(character):
    
    regexNumericAndCharacter = re.compile('\w')
    result = False
    
    if regexNumericAndCharacter.match(character):
        result = True
    else: 
        result = False
    
    return result


def nextBracket(fx):

    result = 0
    count = 0
 
    
    for i in range(0,len(fx)):
        character = fx[i]
        
        if character == '(':
            result = i
            count = count+1
            
        elif character == ')':   
            result = i
            count=count-1
            if count == 0:
                return i
        else:
            result=i        
        
    if count !=0:
        raise CalculatorException ("Exception: ( is not finished")
    
    return result
