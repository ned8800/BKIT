
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import *
from lab_python_fp.print_result import *
from lab_python_fp.cm_timer import *



goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'зеленый'},
    {'title': 'Диван для отдыха', 'color': 'черный'},
    {'title': 'Кресло', 'price': 7000, 'color': 'желтый'},
    {'title': 'Ковер', 'price': 2000, 'color': 'зеленый'}
]


if __name__ == '__main__':

    Vas = field(goods, "title", "price")
    for i in Vas:
         print(i)
    print()

    a = gen_random(5, 1, 3)
    while True:
        try:
            print(next(a))
        except StopIteration:
            break

    print()
    vas = gen_random(5, 1, 3)
    x = Unique(vas)
    while True:
        try:
            print(next(x))
        except StopIteration:
            break

    print()
    result = sorted((abs(x) for x in data), reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)

    print()
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
    print()

    with cm_timer_1("in", "out"):
        time.sleep(1.5)

    with cm_timer_2("in", "out"):
        time.sleep(1)
    print()
