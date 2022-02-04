# python.math.expression.parser.pymep

pymep can parse or evaluate math expressions and it is tested using matlab/octave

This algorithm does not use a decision tree. It is a kind of Recursive Ascent Parser (https://en.wikipedia.org/wiki/Recursive_ascent_parser). In fact, it is LR parser (Left-Right Parser) without backtracking. This recursive algorithm is faster than decision trees

## pypi version

  https://pypi.org/project/pymep/

## Installation

pip install pymep

## Features

### math functions
- sin, cos, tan, sinh, cosh, tanh, asin, acos, atan, log, log10, sqrt
- pi, e
- real or complex numbers

### parentheses 
    fx= 2*(e*2)
    
### variables 

- Expressions in vars

      var = {"x":"1+2+3+4+5", "Z":1}
      eval(" 2*(-(((z*3)*sqrt(x^(2)))+3))",var)





## Examples

### Parse or eveluate expressions with real numbers:    
	
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
	

### Parse or evaluate expressions with complex numbers:
  
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
 
 
 ## How to execute the tests 
 
	from pymep.realParserTest import functionXTest;

	p = functionXTest();

	p.test_one();
	p.test_three();
	
 ## Vulnerabilities
 
	Zero vulnerabilities on https://snyk.io/vuln/pip:pymep

 ## Notes
 - The java version of this library is: https://github.com/sbesada/java.math.expression.parser
 - Regarding to the OS where you excute the tests, it is possible that some tests fail beacause of rounding issues. The mathematical library that was used in this project is "math". In the future, it is possible that the math library changes. 

## Professional Services
If you are interested in logical parsers or any task related to parsers, you can consult my professional services page https://github.com/sbesada/professional.services        

## Donation
If you think that my work deserves a donation, you can do it: https://sbesada.github.io/
