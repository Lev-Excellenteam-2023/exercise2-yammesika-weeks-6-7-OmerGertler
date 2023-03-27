# Author: Omer Gertler

import timeit


def timer(f, *params, **optionals):
    """
    Calculates execution time in milliseconds of a given function and it's parameters.
    The function can get any number of parameters and named parameters.
    The return value is a string of the execution time and the details of the function.
    For example: for: timer(zip, [1, 2, 3], [4, 5, 6])
                 the output is: execution time is: 0.0091000000 ms  ---->  function: zip(([1, 2, 3], [4, 5, 6]), {})
    :param f: any function
    :param params: the parameters of the function
    :param optionals: the named parameters of the function
    :return: string of the execution time of the function
    """
    exec_time = timeit.timeit(lambda: f(*params, **optionals), number=10)
    return f'execution time is: {exec_time * 10**3:.10f} ms  ---->  function: {f.__name__}({params}, {optionals})'


print(timer(print, "Hello"))
print(timer(zip, [1, 2, 3], [4, 5, 6]))
print(timer("Hi {name}".format, name="Bug"))
