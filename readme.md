Python 3.7.3


###calc.py
Main file to run this calculator engine.
Runs the engine in command line, with one valid argument as input.

Example:
1. $ python calc.py "123"
2. $ python calc.py "(add 12 12)"

Content:
1. Make sure this engine has an argument as input. Instantiate a ParseInput object(instance) to parse the input into a more understandable list.
3. Instantiate an Expression instance called expression, then calculator will use this instance.Check if this expression is a valid S_expression.
5. If it is a valid expression, instantiate a calculator using Calculator object. Then print the calculated result.



###parse.py
ParseInput is an Object to read and parse the input string.

Input string is from command line argument, like:
"(multiply (add 1 2) 3)"

**Use pasre_to_list()** method to parse the string into a list, like:
['(', 'multiply', '(', 'add', '1', '2', ')', '3', ')']




###calculator.py
Calculator is an Object that can parse the Expression instance and give the calculated result.

Use **calculate()** method to calculate, input of this method is an Expression instance, output is a number(integer).
**calc_add()** method and **calc_mul()** method do add and multiply calculation respectively.



###expr.py
Expression is an Object that stores the expression list and does basic manipulation on it.

**check_validation()** method checks whether an expression is a valid S_expression.
**get_subexprs()** method gets sub expressions for a function expression, and returns a list of expressions(here not Expression instance, just expression list). This method makes sure the recursive process in both checking expression validation and calculation.