from expr import *

class Calculator(object):

    def __init__(self):
        pass

    def calculate(self, expression):
        return self.calc_expression(expression)


    def calc_expression(self, expression):
        if not expression:
            print('Sorry, you need to load expression!')
            return

        if expression.get_length() == 1:
            return expression.get_int()

        operator = expression.get_operator()

        if operator == 'add':
            return self.calc_add(expression)

        if operator == 'multiply':
            return self.calc_mul(expression)



    def calc_add(self, expression):
        base = 0
        for subexpr in expression.get_subexprs(expression.get_exprlist()):
            base += self.calc_expression(Expression(subexpr))
        return base


    def calc_mul(self, expression):
        base = 1
        for subexpr in expression.get_subexprs(expression.get_exprlist()):
            base *= self.calc_expression(Expression(subexpr))
        return base
