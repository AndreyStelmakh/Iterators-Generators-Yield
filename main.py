from collections.abc import Iterable


class FlatIterator:
    lst = []

    def __init__(self, n_list):
        def unnest(list_):
            tmp = []
            for item_ in list_:
                if isinstance(item_, Iterable) and not isinstance(item_, str):
                    tmp.extend(unnest(item_))
                else:
                    tmp.extend([item_])

            return tmp

        self.lst = unnest(n_list)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lst) == 0:
            raise StopIteration

        return self.lst.pop(0)


def flat_generator(n_list):
    for item_ in n_list:
        if isinstance(item_, Iterable) and not isinstance(item_, str):
            yield from flat_generator(item_)
        else:
            yield item_


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
    [['i', 'j', ['k', 'l']], 'm', ['n', 'o', ['p', ['q']]]]]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)

    print("*" * 20)

    for item in flat_generator(nested_list):
        print(item)

    print("*" * 20)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print("*" * 20)

    flat_list_2 = [item for item in flat_generator(nested_list)]
    print(flat_list_2)
