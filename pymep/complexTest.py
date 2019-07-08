from __future__ import absolute_import

import unittest
from .complex import Complex


class ComplextTest(unittest.TestCase):

    def test_methods(self):
        a = Complex(1,2);
        b = Complex(3,4);
        
        print("abs")   
        print(a.__abs__())
        print(Complex.abs(a))
       
        print("acos")         
        print(a.__acos__().__complex__())
        
        print("add")
        print(a.__add__(b).__complex__())
        print(Complex.add(a,b).__complex__())
        
        print("arg")
        print(a.__arg__())      
        
        print("asin")
        print(a.__asin__().__complex__())
        
        print("atan")
        print(a.__atan__().__complex__())
        
        #print("atanh")
        #print(a.__atanh__().__complex__())
        
        print("cos")
        print(a.__cos__().__complex__())
        
        print("cosh")
        print(a.__cosh__().__complex__())
        
        print("conjugate")
        print(a.conjugate().__complex__())
        print(Complex.sconjugate(a).__complex__())
        
        print("div")
        print(a.__div__(b).__complex__())
        print(Complex.div(a, b).__complex__())
        
        print("exp")
        print(a.__exp__().__complex__())
        
        print("inverse")
        print(a.__inverse__().__complex__())
        
        print("log")
        print(a.__log__().__complex__())
        
        print("log10")
        print(a.__log10__().__complex__())
        
        print("module")
        print(a.__module__())
        
        print("mul")
        print(a.__mul__(b).__complex__())
        print(Complex.mul(a, b).__complex__())
        
        print("neg")
        print(a.__neg__().__complex__())
        
        print("pow")
        print(a.__pow__(b).__complex__())
        print(Complex.pow(a, b).__complex__())
        
        print("radd")
        print(a.__radd__(10).__complex__())
        print(Complex.radd(10, a).__complex__())
        
        print("rdiv")
        print(a.__rdiv__(10).__complex__())
        print(Complex.rdiv(10, a).__complex__())
        
        print("rmul")
        print(a.__rmul__(10).__complex__())
        print(Complex.rmul(10, a).__complex__())
        
        print("rpow")
        print(a.__rpow__(10).__complex__())
        print(Complex.rpow(10, a))
        
        print("rsub")
        print(a.__rsub__(10).__complex__())
        print(Complex.rsub(10, a).__complex__())
        
        print("sin")
        print(a.__sin__().__complex__())
        
        print("sinh")
        print(a.__sinh__().__complex__())
        
        print("sqrt")
        print(a.__sqrt__().__complex__())
        print(Complex.sqrt(a))
        
        print("sub")
        print(a.__sub__(b).__complex__())
        print(Complex.sub(a, b).__complex__())
        
        print("tan")
        print(a.__tan__().__complex__())
        
        print("tanh")
        print(a.__tanh__().__complex__())
        
              
        self.assertTrue(True)
        
   
  

if __name__ == '__main__':
    unittest.main()
