# Author: Omer Gertler


def group_by(f, iterable):
    """
    Implementation of group-by method.
    Make a dictionary when the keys are the return values of "f" with the
    parameters of "iterable" items. The values are the iterable-items that
    belong to the key.
    Example: input: group_by(len, ["hi", "bye", "yo", "try"])
             output: {2: ['hi', 'yo'], 3: ['bye', 'try']}
    :param f: function to group-by it
    :param iterable: items for grouping
    :return: dictionary {<group-bi-it value>: [<items>]}
    """
    d = {}
    for i in iterable:
        key = f(i)
        if key not in d.keys():
            d[key] = [i]
        else:
            d[key].append(i)
    return d


res = group_by(len, ["hi", "bye", "yo", "try"])
print(res)
