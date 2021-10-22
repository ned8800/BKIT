goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'зеленый'},
    {'title': 'Диван для отдыха', 'color': 'черный'},
    {'title': 'Кресло', 'price': 7000, 'color': 'желтый'},
    {'class': 'human', 'name': 'Bob'}
]


def field(items, *args):
    assert (len(args) > 0)
    if len(args) == 1:
        for arg in args:
            for i in range(len(items)):
                for it in items[i]:
                    if it ==arg and items[i][it] != None:
                        yield items[i][it]
    else:
        for i in range(len(items)):
            d = {}
            for arg in args:
                for it in items[i]:
                    if it == arg:
                        d[it] = items[i][it]
            yield d

if __name__ == '__main__':

    Vas = field(goods, "title", "price", "color")
    for i in Vas:
         print(i)
    print()
