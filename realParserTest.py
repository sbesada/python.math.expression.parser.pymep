import unittest
from realParser import evalXi
from realParser import parse


class functionXTest(unittest.TestCase):
    
    def test_one(self):
      
        self.assertEqual(7, parse("((2)+(5))"))
        self.assertEqual(-3, parse(" (2)-(5)"))
        self.assertEqual(28, parse("+3 +5*5*(+1)"))        
        self.assertEqual(25, evalXi("5*(x +3)",2))
        self.assertEqual(25, evalXi("5*(x +3)",2))
        self.assertEqual(25, evalXi("5*(x +3)","1+1"))
        self.assertEqual(0.2339992213289606, evalXi("(2.35*e^(-3)*x)",2))
        self.assertEqual(0.9092974268256817, evalXi("sin(x)",2))
        var = {"x":2, "Z":1}
        self.assertEqual(-18.0, evalXi(" 2*(-(((z*3)*sqrt(x^(2)))+3))",var))
        
        var = {"x":"1+1", "Z":1}
        self.assertEqual(-18.0, evalXi(" 2*(-(((z*3)*sqrt(x^(2)))+3))",var))
        var2 = {"x":"1+1", "Z":"cos(1)"}
        self.assertEqual(evalXi(" 2*(-(((cos(z)*3)*sqrt(x^(2)))+3))",var), evalXi(" 2*(-(((z*3)*sqrt(x^(2)))+3))",var2))
        self.assertEqual(evalXi(" 2*(-(((cos(z)*3)*sqrt(x^(2)))+3))",var),-12.483627670417677)
        self.assertEqual(-12.483627670417677, evalXi(" 2*(-(((z*3)*sqrt(x^(2)))+3))",var2))
                       
    def test_two(self): 
   
        f_x = "5*(2*(sqrt((x+2)^2)) +3)"
        x0 = 2
        self.assertEqual(55, evalXi(f_x, x0))
        
        f_x = "5*(2*(sqrt((x+2)^2)/2) +3)";
        self.assertEqual(35, evalXi(f_x, x0))
        
        f_x = "cosh(6+(2/0))"
        
        #self.assertEqual(-1, evalXi(f_x, x0))
      
        f_x = "cos(x)"
        x2 = 0 
        self.assertEqual(1, evalXi(f_x, x2))
        
        
    def test_three(self):
        
        
        f_x = "+3 +5*5*(+1)";
        self.assertEqual(28, parse(f_x))

        f_xs = "x+5*y+(3 -y)"
        var = {"x":"1+1*1", "y":1}
       
        self.assertEqual(9, evalXi(f_xs,var))
        
        
        
    def test_four(self):
        
        
        f_x = "log(e)";
        self.assertEqual(1, parse(f_x))

        f_x = "log10(x)"
        var = {"x":"5*2 +10 -10"}
        self.assertEqual(1, evalXi(f_x,var))
        
        f_x=" 1 + acos(0.1)"
        self.assertEqual(2.470628905633337, parse(f_x))        
        
        var = {"x":2, "y":3.1}       
        f_x = " ((2+x)^2) + cos((3/2+2*y)^(0.5*x))"
        self.assertEqual(16.153373862037864, evalXi(f_x,var))     

     
if __name__ == '__main__':
    unittest.main()

