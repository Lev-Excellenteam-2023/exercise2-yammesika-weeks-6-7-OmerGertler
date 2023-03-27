# Omer Gertler
# decorator factory for checking parameter's type

from functools import wraps


def type_check(correct_type):
    """ Check type of an argument"""
    def dec(fn):
        @wraps(fn)
        def inner(arg):
            """  A wrapper function. """
            if isinstance(arg, correct_type):
                res = fn(arg)
                print(res)
                print(f'Check-type result: {True} (Except: {correct_type}, got: {correct_type}\n')
            else:
                raise CustomError(correct_type, type(arg))
        return inner
    return dec


@type_check(int)
def times2(num):
    """ Return num*2 """
    return num * 2


class CustomError(Exception):
    """ My exception for type-check function. """

    def __init__(self, correct_type, arg_type, *args):
        super().__init__(args)
        self.correct_type = correct_type
        self.arg_type = arg_type

    def __str__(self):
        return f'Error! except: {self.correct_type} got: {self.arg_type}'


try:
    print(f'The function name: {times2.__name__}')
    print(f'The function docstring: {times2.__doc__}\nFunction output:')
    times2(2)
    times2('2')
except CustomError as ex:
    print(ex)
