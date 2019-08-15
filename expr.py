class Expression(object):

    def __init__(self, expr_list=None):
        self.__expression = expr_list


    def get_subexprs(self, expr_list):
        res = []
        i = 2
        while i < len(expr_list)-1:
            l = self.count_subexpr_length(expr_list, i)
            res.append(expr_list[i:i+l])
            i += l
        return res


    def count_subexpr_length(self, expr_list, i):
        j = i+1
        if expr_list[i] == '(':
            count = 1
            while count!= 0 and j<len(expr_list):
                if expr_list[j] == ')':
                    count -= 1
                if expr_list[j] == '(':
                    count += 1
                j += 1
        return j-i


    def check_validation(self):
        return self.is_valid(self.__expression)


    def is_valid(self, expr_list):
        if not expr_list:
            return False
        if len(expr_list)==1:
            return self.is_integer(expr_list)
        return self.is_func(expr_list)


    def is_func(self, expr_list):
        if len(expr_list) < 4:
            return False
        if expr_list[0] != '(' or expr_list[-1] != ')':
            return False
        if expr_list[1] not in ['add', 'multiply']:
            return False

        count = 0
        for char in expr_list:
            if char == '(':
                count += 1
            if char == ')':
                count -=1
                if count <0 :
                    return False
        if count != 0 :
            return False 

        for subexpr in self.get_subexprs(expr_list):
            if not self.is_valid(subexpr):
                return False
        return True


    def is_integer(self, expr_list):
        return expr_list[0].isdigit()


    def get_length(self):
        return len(self.__expression)


    def get_int(self):
        if len(self.__expression) == 1:
            return int(self.__expression[0])


    def get_operator(self):
        if len(self.__expression) > 1 :
            return self.__expression[1]


    def get_exprlist(self):
        return self.__expression
