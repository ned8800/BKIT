from lab_python_fp.field import field

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'зеленый'},
    {'title': 'Диван для отдыха', 'color': 'черный'},
    {'title': 'Кресло', 'price': 7000, 'color': 'желтый'},
    {'title': 'Ковер', 'price': 2000, 'color': 'зеленый'}
]

def unify(v):
    return str(v).lower().strip()

class Unique(object):
    n = 0

    def __init__(self, items, ignore_case=False):
        self.ignore_case = ignore_case
        self.data = items
        self.dict = []
        if ignore_case == False:
            for i in items:
                if i not in self.dict:
                    self.dict.append(i)
        else:
            for i in items:
                if unify(i) not in self.dict:
                    self.dict.append(unify(i))



    def __next__(self):
        if self.n < len(self.dict):
            x = self.dict[self.n]
            self.n += 1
            return x
        else:
            raise StopIteration

    def __iter__(self):
        return self

if __name__ == '__main__':

    data1 = ['dDDdDa', "AAA", 'bbb', 'aaa', 'CCccC', 'aaa', 'ccccc']
    data2 = [8, 7, 7, 1, 1, 2, 1, 3, 4, 5, 6]
    for u in Unique(data1, ignore_case=True):
        print(u, end=' ')
    print('\n')
    for u in Unique(data1):
        print(u, end=' ')
    print('\n')
    for u in Unique(data2):
        print(u, end=' ')
