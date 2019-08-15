class ParseInput(object):

    def __init__(self, input_string=''):
        self.input_string = input_string

    def parse_to_list(self):
        if self.input_string == '':
            print('No Valid Input!')
            return None

        newString = ''
        for char in self.input_string:
            if char == '(':
                newString += char + ' '
            elif char == ')':
                newString += ' ' + char
            else:
                newString += char

        return newString.split()
