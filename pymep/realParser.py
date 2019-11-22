from .exception import CalculatorException
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
    
    i = 0
    
    while (i < len(fx)):
        character = fx[i]
        
        if character == '*':     
            if hasNumber == True:
                numb = number
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = float(numb) * float(eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            elif hasFunction == True:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = float(eval(function, xi)) * float(eval(new_fx, xi))
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = float(value) * float(eval(new_fx, xi))
                i = i + len(new_fx)
         
         
        elif character == '+':   
    
            if hasNumber == True:
                numb = number
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = float(numb) + float(eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            elif hasFunction == True:
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = float(eval(function, xi)) + float(eval(new_fx, xi))
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = float(value) + float(eval(new_fx, xi))
                i = i + len(new_fx)
                
                   
        elif character == '-':   
    
            if hasNumber == True:
                numb = number
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = float(numb) - float(eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            elif hasFunction == True:
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = float(eval(function, xi)) - float(eval(new_fx, xi))
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextMinusFunction(fx[i + 1:len(fx)])
                value = float(value) - float(eval(new_fx, xi))
                i = i + len(new_fx)
                
        elif character == '/':     
            if hasNumber == True:
                numb = number
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = float(numb) / float(eval(new_fx, xi))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            elif hasFunction == True:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = float(eval(function, xi)) / float(eval(new_fx, xi))
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = float(value) / float(eval(new_fx, xi))
                i = i + len(new_fx)
    
        elif character == '^':     
            if hasNumber == True:
                numb = number
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = math.pow(float(numb), float(eval(new_fx, xi)))
                i = i + len(new_fx)
                hasNumber = False
                number = ""
            elif hasFunction == True:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = math.pow(float(eval(function, xi)),float(eval(new_fx, xi)))
                i = i + len(new_fx)
                hasFunction = False
                function = ""
            else:
                new_fx = nextFunction(fx[i + 1:len(fx)])
                value = math.pow(float(value),float(eval(new_fx, xi)))
                i = i + len(new_fx)
                
        elif character == '0' or character == '1' or character == '2' or character == '3' or character == '4' or character == '5' or character == '6' or character == '7' or character == '8' or character == '9':
            
            if hasFunction == True:
                function = function + character
               
            else:        
                hasNumber = True
                number = number + character
                if i == len(fx) - 1:
                    value = number
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
                    value = math.sin(float(eval(new_fx, xi)))                        
    
                elif function == "cos":
                    value = math.cos(float(eval(new_fx, xi)))
                    
                elif function == "tan":
                    value = math.tan(float(eval(new_fx, xi)))
                
                elif function == "sinh":
                    value = math.sinh(float(eval(new_fx, xi)))
                
                elif function == "cosh":
                    value = math.cosh(float(eval(new_fx, xi)))
    
                elif function == "tanh":
                    value = math.tanh(float(eval(new_fx, xi)))
    
                elif function == "asin":
                    value = math.asin(float(eval(new_fx, xi)))
                    
                elif function == "acos":
                    value = math.acos(float(eval(new_fx, xi)))  
                                          
                elif function == "atan":
                    value = math.atan(float(eval(new_fx, xi)))
                    
                elif function == "log":
                    value = math.log(float(eval(new_fx, xi)))
                    
                elif function == "log10":
                    value = math.log10(float(eval(new_fx, xi)))
                    
                elif function == "sqrt":                    
                    value = math.sqrt(float(eval(new_fx, xi)))
                    
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
        else:
            if isValidCharacter(character):
                function = function + character
                hasFunction = True
    
                if i == len(fx) - 1:
    
                    if function == "e":
                        value = math.e
    
                    elif function == "pi":
                        value = math.pi
                    
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
            value = xi
        elif isinstance(xi, float):
            value = xi
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
