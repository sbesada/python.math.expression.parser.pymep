import unittest
from .complex import Complex
from .complexParser import eval
from .complexParser import parse


class functionXTest(unittest.TestCase):
    
    def test_one(self):
      
        f_x = "1+j"
        self.assertEqual(complex(1,1), parse(f_x).__complex__())
        
        f_x = "1+j*3"
        self.assertEqual(complex(1,3), parse(f_x).__complex__())
        
        f_x = "(1+2i)*3"
        self.assertEqual(complex(3,6), parse(f_x).__complex__())
    
        f_x = "(1+j)*3"        
        self.assertEqual(complex(3,3), parse(f_x).__complex__())

        f_x = "(1+2i)^3"        
        #self.assertEqual(complex(-11,-2), parse(f_x).__complex__())

        f_x = "log((1-2i)^3)"
        self.assertEqual(complex(2.4141568686511508,2.9617391537973154), parse(f_x).__complex__())

        f_x = "log10((1-2i)^3)"
        self.assertEqual(complex(1.0484550065040283,1.2862669713309804), parse(f_x).__complex__())

        f_x = "sqrt((1-2i)^3)"        
        self.assertEqual(complex(0.30028310600077657,3.3301906767855614), parse(f_x).__complex__())

        f_x = "sin((2*3-2i)^0.5)"
        self.assertEqual(complex(0.6628558929948344,0.3271184710098071), parse(f_x).__complex__())

        f_x = "tan((3/2-2i)^(1+j))"
        self.assertEqual(complex(0.03543314322660282,-0.0695134023467424), parse(f_x).__complex__())
        
        f_x = "2*sinh((3/2-2i)^(i+j))"
        self.assertEqual(complex(-5.00258977693665,-0.6042432287388212), parse(f_x).__complex__())

        f_x = "(2+i)*cosh((3/2-2i)^(i+2j))"
        self.assertEqual(complex(2847048.2544272062,1810397.8937584711), parse(f_x).__complex__())
  
        f_x = " ((2+i)^2)/tanh((3/2-2i)^(i+2j))"
        #self.assertEqual(complex(-3,4), parse(f_x).__complex__())

        f_x = " ((2+i)^2) -asin((3/2-2i)^(i+2j))"
        self.assertEqual(complex(4.177396646578185,0.5256449471598219), parse(f_x).__complex__())
  
        fx=" 1 + acos(0.1)"
        self.assertEqual(complex(2.470628905633337,0), parse(fx).__complex__())

        f_x = " ((2+i)^2) + acos((3/2-2i)^(5+2j))"
        self.assertEqual(complex(5.803894224758176,11.129190774731054), parse(f_x).__complex__())
        
        f_x = " ((2+i)/2) + atan((3/2-2i)^(5/2j))"        
        self.assertEqual(complex(0.9348271503983473,0.42616088672356495), parse(f_x).__complex__())
        
        f_x = " e^(acos((3/2-2i)^(5+2j)))"
        self.assertEqual(complex(10.944992983920486,12.359124636924806), parse(f_x).__complex__())
        
        f_x = " e^(acos((3/2-2i)^(pi)))"
        self.assertEqual(complex(-16.73722931144932,-7.665052576046686), parse(f_x).__complex__())
      
       
    def test_two(self):
      
        f_x = " e^(1*x*acos((3/2-2i)^(pi)))"
        x0 = "1 +j"
        x1 = Complex(1,1)
        x2 = complex(1,1)
        self.assertEqual(complex(0.5073815520994653,0.10322073421674559), eval(f_x,x0).__complex__())
        self.assertEqual(complex(0.5073815520994653,0.10322073421674559), eval(f_x,x1).__complex__())
        self.assertEqual(complex(0.5073815520994653,0.10322073421674559), eval(f_x,x2).__complex__())
        
     
        var={"x":"1+2j", "Y":complex(2,1)}
        f_x = "x+j"
        self.assertEqual(complex(1,3), eval(f_x,var).__complex__())
      
        
        f_x = "x-y";
        self.assertEqual(complex(-1,1), eval(f_x,var).__complex__())
        
        f_x = " e^(1*x*y*acos((3/2)^(pi)))"
        self.assertEqual(complex(5.92391246725083e-05,0), eval(f_x,var).__complex__())
        
        f_x = " e^(1*x*y*sin((3/2)^(pi)))"
        self.assertEqual(complex(-0.5024692307417822,-0.864595091449033), eval(f_x,var).__complex__())
      
      
      
        
        
        
if __name__ == '__main__':
    unittest.main()

