# python.math.expression.parser.pymep

pymep can parse or evaluate math expressions.

This algorithm does not use a decision tree. It is a recursive algorithm that is faster than decision trees

Installation

pip install pymep

Here you can see some examples:

  Real Numbers:    
	
	from pymep.realParser import parse
	from pymep.realParser import eval


	#Real Expresion parser
	fx="cos(10)"
	print(parse(fx))
	
	xi=5
	fx = "1 + x"
	print(eval(fx, xi))
	
	var = {"x":"1+1", "Z":1}
	eval(" 2*(-(((z*3)*sqrt(x^(2)))+3))",var)
	

  For Complex Numbers:
  
    from pymep.complexParser import parse
	from pymep.complexParser import eval
	from pymep.complex import Complex

	#Operation with complex numbers
	a = Complex(1,2)
	print(a.__radd__(10).__complex__())
	print(Complex.radd(10, a).__complex__())


	#Complex Expresion parser
	fx="cos(10+2j)"
	print(parse(fx).__complex__())
	
	xi=5
	fx = "1 +j+x"
	print(eval(fx, xi).__complex__())
	
	var={"x":"1+2j", "Y":complex(2,1)}
	f_x = "x-y"
	eval(f_x,var).__complex__()
	
    
 There is a full list of examples inside!!

Enjoy it!!

The java version of this library is: https://github.com/sbesada/java.math.expression.parser

NOTE: Regarding to the OS where you excute the tests, it is possible that some tests fail due to rounding issues. The mathematical library used in this project is "math". In the future, it is possible that the math library changes. 

PD: If you think that my work deserves a donation, you can do it: https://sbesada.github.io/
