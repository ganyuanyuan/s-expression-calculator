import sys
from parse import *
from expr import *
from calculator import *

def main():
    if len(sys.argv)<2:
        print('No Input!')
        return

    expr_list = ParseInput(sys.argv[1]).parse_to_list()
    expression = Expression(expr_list)

    if not expression.check_validation():
        print('Not Valid Input!')
        return

    calculator = Calculator()
    print(calculator.calculate(expression))



if __name__ == '__main__':
    main()
