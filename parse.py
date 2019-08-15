class ParseInput(object):

    def __init__(self, inputString=''):
        self.inputString = inputString

    def parse_to_list(self):
        if self.inputString == '':
            print('No Valid Input!')
            return None

        newString = ''
        for char in self.inputString:
            if char == '(':
                newString += char + ' '
            elif char == ')':
                newString += ' ' + char
            else:
                newString += char

        return newString.split()
