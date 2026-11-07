import types
from datetime import datetime


def logger(old_function):


    def new_function(*args, **kwargs):


        result = old_function(*args, **kwargs)

        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(f'{date}\n')
            f.write(f'{old_function.__name__},\n')
            f.write(f'{args}, {kwargs}\n')
            f.write(f'{result}')

        return result

    return new_function
@logger
def flat_generator(list_of_lists):

    for item in list_of_lists:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
