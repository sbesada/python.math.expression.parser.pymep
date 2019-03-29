from numbers import Complex
from exception import CalculatorException
import math

class Complex(Complex):    
    
    def __init__(self, real=0.0, imag=0.0):
        self.real=real
        self.imag=imag        
    
    def imag(self):
        return self.imag      
  
    def real(self):
        return self.real        
    
    def __abs__(self):
        
        x = abs(self.real)
        y = abs(self.imag)
        
        if x == 0.0:
            return y
        elif y == 0.0:
            return x
        elif x > y:
            temp = y / x
            return x * math.sqrt(1.0 + (temp * temp))
        else:
            temp = x / y
            return y * math.sqrt(1.0 + (temp * temp))
    
   
    def __add__(self,b):
        r= self.real+b.real
        i= self.imag + b.imag
          
        return Complex(r,i)
    
    def __complex__(self):
        return complex(self.real,self.imag)
    
    def __eq__(self):
        raise NotImplementedError
    
    def __mul__(self,c):
        r = (self.real * c.real) - (self.imag * c.imag)
        i = (self.imag * c.real) + (self.real * c.imag) 
        
        return Complex(r,i)
    
    
    def __neg__(self):
        return Complex(-self.real, -self.imag)
    
    def __pos__(self):
        raise NotImplementedError
    
    def __pow__(self,exp):
        a = self.__log__()
        a = self.mul(exp, a)
        return a.__exp__()     
    
    def __radd__(self,real):
        r= real+ self.real       
        
        return Complex(r,self.imag)
    
    def __rmul__(self, real):
        r = self.real * real
        i = self.imag * real
        
        return Complex(r,i)
        
    def __rpow__(self,exp):
        a = self.__log__()
        a = self.rmul(exp, a)
        return a.__exp__()
    
    
    def __rsub__(self, real):            
        r= self.real-real       
        return Complex(r,self.imag)
    
    
    def __div__(self,cmpx):
         
        if cmpx.real == 0 and cmpx.imag == 0:
            raise CalculatorException("The complex number b is 0")
         
        c = math.pow(cmpx.real, 2)
        d = math.pow(cmpx.imag, 2)
        
        r = (self.real * cmpx.real) + (self.imag * cmpx.imag)
        r /= (c + d)
        
        i = (self.imag * cmpx.real) - (self.real * cmpx.imag)
        i /= (c + d)
        
        return Complex(r,i)
   
  
    def __rdiv__(self, real):
        if real == 0:
            raise CalculatorException("scalar is 0")
          
        r = self.real / real
        i = self.imag / real
        
        return Complex(r,i)
    
    def __rtruediv__(self):
        raise NotImplementedError
    
    def __truediv__(self):
        raise NotImplementedError
    
    def conjugate(self):
        return Complex(self.real, -self.imag)

    def __inverse__(self):        
         
        a = self.real * self.real
        b = self.imag * self.imag
        
        if a == 0.0 and b == 0.0:
            return Complex()
        else:
            r= self.real / (a + b)
            i= self.imag / (a + b)
            return Complex(r,i)
    
    def __log__(self):
        return Complex(math.log(self.abs(self)), math.atan2(self.imag, self.real))
    

    #E^c 
    def __exp__(self):
        exp_x = math.exp(self.real)
        return Complex(exp_x * math.cos(self.imag), exp_x * math.sin(self.imag))        
     
     
    def __module__(self):
        return math.sqrt((self.real * self.real) + (self.imag * self.imag))
    
    
    def __arg__(self):
        angle = math.atan2(self.imag, self.real)
        print (angle)
        if angle < 0.0:
            angle = (2 * math.pi) + angle
        
        return (angle * 180) / math.pi

    
    def __log10__(self):

        rpart = math.sqrt((self.real * self.real) + (self.imag * self.imag))
        ipart = math.atan2(self.imag,self.real)
        if ipart > math.pi:
            ipart = ipart - (2.0 * math.pi)
        
        return Complex(math.log10(rpart), (1 /math.log(10)) * ipart)

    
    
    

    def __sqrt__(self):
        r = math.sqrt((self.real * self.real) + (self.imag * self.imag))
        rpart = math.sqrt(0.5 * (r + self.real))
        ipart = math.sqrt(0.5 * (r - self.real))
        if self.imag < 0.0:
            ipart = -ipart
        
        return Complex(rpart, ipart)
     
    
    def __sin__(self):
        return Complex(math.sin(self.real) * math.cosh(self.imag), math.cos(self.real) * math.sinh(self.imag))
    
    def __cos__(self):
        return Complex(math.cos(self.real) * math.cosh(self.imag), -math.sin(self.real) * math.sinh(self.imag))
    
    def __tan__(self):
        return self.div(self.__sin__(), self.__cos__())
    
    def __asin__(self):
        im = Complex(0.0, -1.0)
        zp = self.mul(self, im)
        zm = self.add((self.sub(Complex(1.0, 0.0), self.mul(self, self))).__sqrt__(), zp)
        return self.mul(zm.__log__(), Complex(0.0, 1.0))
    
    def __acos__(self):
        im = Complex(0.0, -1.0)
        zm = self.add(self.mul((self.sub(Complex(1.0, 0.0), self.mul(self, self))).__sqrt__(), im), self)
        return self.mul(zm.__log__(), Complex(0.0, 1.0))
    
    def __atan__(self):
        
        im = Complex(0.0, -1.0);
        zp= Complex(self.real, self.imag - 1.0);
        zm = Complex(-self.real, -self.imag - 1.0);
        aux = self.div(zp, zm).__log__()
       
        aux2 = self.mul(im, aux)
       
        return self.rdiv(2.0, aux2)
         
    
    def __sinh__(self):
        return Complex(math.sinh(self.real) * math.cos(self.imag), math.cosh(self.real) * math.sin(self.imag))
    
    def __cosh__(self):
        return Complex(math.cosh(self.real) * math.cos(self.imag), math.sinh(self.real) * math.sin(self.imag))
    
    def __tanh__(self): 
        return self.div(self.__sinh__(), self.__cosh__())
    
    def __atanh__(self):
      
        #aux1 = self.add(1.0, self).__log__()
        #aux21 = self.rsub(1.0, self)
        #aux22 = aux21.__neg__()
        #aux2 = self.rdiv(2.0, aux22.__log__())
        
        #return self.sub(aux1,aux2)
        raise NotImplementedError
    
       
    
    @staticmethod
    def add(a, b):
            
        r= a.real+b.real
        i= a.imag + b.imag
        
        return Complex(r,i)
    
    # @staticmethod
    #def cbrt(self,c):
        
    #    if c.imag != 0.0:
    #       real = math.cbrt(self.abs(c)) * math.cos(c.__arg__() / 3.0)
    #        imag = math.cbrt(self.abs(c)) * math.sin(c.__arg__() / 3.0)
    #        return Complex(real,imag)
    #    else:
    #        return Complex(math.cbrt(c.real), 0)
    
       
    @staticmethod
    def radd(real, c):
            
        r= c.real+ real       
        
        return Complex(r,c.imag)
    
    @staticmethod
    def sub(a, b):
            
        r= a.real-b.real
        i= a.imag - b.imag  
        
        return Complex(r,i)
    
    @staticmethod
    def rsub(real, c):
            
        r= c.real-real         
        
        return Complex(r,c.imag)
    
    @staticmethod
    def mul(a, b):
            
        r = (a.real * b.real) - (a.imag * b.imag)
        i = (a.imag * b.real) + (a.real * b.imag) 
        
        return Complex(r,i)
    
    
    @staticmethod
    def rmul(real, c):
            
        r = c.real * real
        i = c.imag * real
        
        return Complex(r,i)
    
    @staticmethod
    def sconjugate(c):
        return Complex(c.real, -c.imag)

    @staticmethod
    def div(a, b):
         
        if b.real == 0 and b.imag == 0:
            raise CalculatorException("The complex number b is 0")
         
        c = math.pow(b.real, 2)
        d = math.pow(b.imag, 2)
        
        r = (a.real * b.real) + (a.imag * b.imag)
        r /= (c + d)
        
        i = (a.imag * b.real) - (a.real * b.imag)
        i /= (c + d)
        
        return Complex(r,i)
   
    @staticmethod
    def rdiv(real, c):
        if real == 0:
            raise CalculatorException("scalar is 0")
          
        r = c.real / real
        i = c.imag / real
        
        return Complex(r,i)
 
   
    @staticmethod
    def abs(c):
        
        x = abs(c.real)
        y = abs(c.imag)
        
        if x == 0.0:
            return y
        elif y == 0.0:
            return x
        elif x > y:
            temp = y / x
            return x * math.sqrt(1.0 + (temp * temp))
        else:
            temp = x / y
            return y * math.sqrt(1.0 + (temp * temp))
    
    @staticmethod
    def sqrt(c):
        
        if c.real == 0.0  and c.imag == 0.0:
            return Complex()
        else: 
            x = abs(c.real)
            y = abs(c.imag)
            r = 0.0
            w = 0.0
            real = 0.0
            imag = 0.0
            if x >= y:
                r = y / x
                w = math.sqrt(x) * math.sqrt(0.5 * (1.0 + math.sqrt(1.0 + (r * r))))
            else:
                r = x / y
                w = math.sqrt(y) * math.sqrt(0.5 * (r + math.sqrt(1.0 + (r * r))))
            
            if c.real >= 0.0:
                real = w
                imag = c.imag / (2.0 * w)
            else:
                imag = w if c.imag >=0 else -w
                real = c.imag / (2.0 * imag)
            
            Complex(real, imag)
   
   
    @staticmethod    
    def rpow(c, exp):
        return c.__rpow__(exp)
    
    
    @staticmethod    
    def pow(c, exp):
        return c.__pow__(exp)
  

    


   



