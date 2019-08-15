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



    # def get_subexprs(self, expression):
    #     res = []
    #     i = 1
    #     while i < len(expression):
    #         l = self.count_subexpr_length(expression, i)
    #         res.append(expression[i:i+l])
    #         i += l
    #     return res
    #
    #
    # def count_subexpr_length(self, expression, i):
    #     j = i+1
    #     if expression[i] == '(':
    #         count = 1
    #         while count!= 0 :
    #             if expression[j] == ')':
    #                 count -= 1
    #             if expression[j] == '(':
    #                 count += 1
    #             j += 1
    #     return j-i
