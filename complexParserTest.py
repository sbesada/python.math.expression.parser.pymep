import unittest
from complex import Complex
from complexParser import evalComplex
from complexParser import parseComplex


class functionXTest(unittest.TestCase):
    
    def test_one(self):
      
        f_x = "1+j"
        self.assertEqual(complex(1,1), parseComplex(f_x).__complex__())
        
        f_x = "1+j*3"
        self.assertEqual(complex(1,3), parseComplex(f_x).__complex__())
        
        f_x = "(1+2i)*3"
        self.assertEqual(complex(3,6), parseComplex(f_x).__complex__())
    
        f_x = "(1+j)*3"        
        self.assertEqual(complex(3,3), parseComplex(f_x).__complex__())

        f_x = "(1+2i)^3"        
        #self.assertEqual(complex(-11,-2), parseComplex(f_x).__complex__())

        f_x = "log((1-2i)^3)"
        self.assertEqual(complex(2.4141568686511508,2.9617391537973154), parseComplex(f_x).__complex__())

        f_x = "log10((1-2i)^3)"
        self.assertEqual(complex(1.0484550065040283,1.2862669713309804), parseComplex(f_x).__complex__())

        f_x = "sqrt((1-2i)^3)"        
        self.assertEqual(complex(0.30028310600077657,3.3301906767855614), parseComplex(f_x).__complex__())

        f_x = "sin((2*3-2i)^0.5)"
        self.assertEqual(complex(0.6628558929948344,0.3271184710098071), parseComplex(f_x).__complex__())

        f_x = "tan((3/2-2i)^(1+j))"
        self.assertEqual(complex(0.03543314322660282,-0.0695134023467424), parseComplex(f_x).__complex__())
        
        f_x = "2*sinh((3/2-2i)^(i+j))"
        self.assertEqual(complex(-5.00258977693665,-0.6042432287388212), parseComplex(f_x).__complex__())

        f_x = "(2+i)*cosh((3/2-2i)^(i+2j))"
        self.assertEqual(complex(2847048.2544272062,1810397.8937584711), parseComplex(f_x).__complex__())
  
        f_x = " ((2+i)^2)/tanh((3/2-2i)^(i+2j))"
        #self.assertEqual(complex(-3,4), parseComplex(f_x).__complex__())

        f_x = " ((2+i)^2) -asin((3/2-2i)^(i+2j))"
        self.assertEqual(complex(4.177396646578185,0.5256449471598219), parseComplex(f_x).__complex__())
  
        fx=" 1 + acos(0.1)"
        self.assertEqual(complex(2.470628905633337,0), parseComplex(fx).__complex__())

        f_x = " ((2+i)^2) + acos((3/2-2i)^(5+2j))"
        self.assertEqual(complex(5.803894224758176,11.129190774731054), parseComplex(f_x).__complex__())
        
        f_x = " ((2+i)/2) + atan((3/2-2i)^(5/2j))"        
        self.assertEqual(complex(0.9348271503983473,0.42616088672356495), parseComplex(f_x).__complex__())
        
        f_x = " e^(acos((3/2-2i)^(5+2j)))"
        self.assertEqual(complex(10.944992983920486,12.359124636924806), parseComplex(f_x).__complex__())
        
        f_x = " e^(acos((3/2-2i)^(pi)))"
        self.assertEqual(complex(-16.73722931144932,-7.665052576046686), parseComplex(f_x).__complex__())
      
       
    def test_two(self):
      
        f_x = " e^(1*x*acos((3/2-2i)^(pi)))"
        x0 = "1 +j"
        x1 = Complex(1,1)
        x2 = complex(1,1)
        self.assertEqual(complex(0.5073815520994653,0.10322073421674559), evalComplex(f_x,x0).__complex__())
        self.assertEqual(complex(0.5073815520994653,0.10322073421674559), evalComplex(f_x,x1).__complex__())
        self.assertEqual(complex(0.5073815520994653,0.10322073421674559), evalComplex(f_x,x2).__complex__())
        
     
        var={"x":"1+2j", "Y":complex(2,1)}
        f_x = "x+j"
        self.assertEqual(complex(1,3), evalComplex(f_x,var).__complex__())
      
        
        f_x = "x-y";
        self.assertEqual(complex(-1,1), evalComplex(f_x,var).__complex__())
        
        f_x = " e^(1*x*y*acos((3/2)^(pi)))"
        self.assertEqual(complex(5.92391246725083e-05,0), evalComplex(f_x,var).__complex__())
        
        f_x = " e^(1*x*y*sin((3/2)^(pi)))"
        self.assertEqual(complex(-0.5024692307417822,-0.864595091449033), evalComplex(f_x,var).__complex__())
      
      
      
        
        
        
if __name__ == '__main__':
    unittest.main()

