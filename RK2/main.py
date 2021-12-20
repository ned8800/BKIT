# используется для сортировки
from operator import itemgetter


class Lib:
    """Библиотека"""

    def __init__(self, id, Lib_name, volum, Lang_id):
        self.Lib_id = id
        self.Lib_name = Lib_name
        self.volum = volum      #Объем в килобайтах
        self.Lang_id = Lang_id


class Lang:
    """Язык программирования"""

    def __init__(self, id, name):
        self.Lang_id = id
        self.Lang_name = name


class Lib_Lang:
    """
    'Библиотеки языков' для реализации
    связи многие-ко-многим
    """

    def __init__(self, Lang_id, Lib_id):
        self.Lang_id = Lang_id
        self.Lib_id = Lib_id


# Языки
Langs = [
    Lang(1, 'Python'),
    Lang(2, 'C++ Lang'),
    Lang(3, 'C# Lang'),

    Lang(11, 'Ruby'),
    Lang(22, 'Swift'),
    Lang(33, 'Pascal'),
]

# Библиотеки
Libs = [
    Lib(1, 'Colorama', 3, 1),
    Lib(2, 'SyST', 14, 2),
    Lib(3, 'EBalance', 4, 3),
    Lib(4, 'Rusty', 8, 3),
    Lib(5, 'XYZ', 10, 3),
]

Libs_Langs = [
    Lib_Lang(1, 1),
    Lib_Lang(2, 2),
    Lib_Lang(3, 3),
    Lib_Lang(3, 4),
    Lib_Lang(3, 5),

    Lib_Lang(11, 1),
    Lib_Lang(22, 2),
    Lib_Lang(33, 3),
    Lib_Lang(33, 4),
    Lib_Lang(33, 5),
]

def Compare_one_to_many(Langs, Libs):
    one_to_many = [(e.Lib_name, e.volum, d.Lang_name)
                   for d in Langs
                   for e in Libs
                   if e.Lang_id == d.Lang_id]
    return one_to_many

def Compare_many_to_many(Langs, Libs):
    many_to_many_temp = [(d.Lang_name, ed.Lang_id, ed.Lib_id)
                         for d in Langs
                         for ed in Libs_Langs
                         if d.Lang_id == ed.Lang_id]

    many_to_many = [(e.Lib_name, e.volum, Lang_name)
                    for Lang_name, dep_id, Lib_id in many_to_many_temp
                    for e in Libs if e.Lib_id == Lib_id]
    return many_to_many

def Task_A2(Langs, one_to_many):
    res_12_unsorted = []
    # Перебираем все языки
    for d in Langs:
        # Сортированный список языков по их имени
        d_Langs = list(filter(lambda i: i[2] == d.Lang_name, one_to_many))
        # Если список не пуст
        if len(d_Langs) > 0:
            # Список из объемов библиотек языка
            d_Libs = [val for _, val, _ in d_Langs]
            # Суммарный объем библиотек языка
            d_Vol_sum = sum(d_Libs)
            res_12_unsorted.append((d.Lang_name, d_Vol_sum))
    # Сортировка по объему
    return sorted(res_12_unsorted, key=itemgetter(1), reverse=True)

def Task_A3(Langs, many_to_many):
    res_13 = {}
    # Перебираем все языки
    for d in Langs:
        if 'Lang' in d.Lang_name:
            # Список библиотек языка программирования
            d_Langs = list(filter(lambda i: i[2] == d.Lang_name, many_to_many))
            # Только название библиотек
            d_Libs_names = [x for x, _, _ in d_Langs]
            # Добавляем результат в словарь
            # ключ - язык, значение - список имен библиотек
            res_13[d.Lang_name] = d_Libs_names
    return res_13

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = Compare_one_to_many(Langs, Libs)

    # Соединение данных многие-ко-многим
    many_to_many = Compare_many_to_many(Langs, Libs)

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    print("#Список связанных библиотек и языков, отсортированный по языкам")

    print('\nЗадание А2')
    res_12 = Task_A2(Langs, one_to_many)
    print(res_12)
    print("#Список языков программирования и суммарного объема их библиотек,")
    print("отсортированный по объему")

    print('\nЗадание А3')
    res_13 = Task_A3(Langs, many_to_many)
    print(res_13)
    print("#Список всех языков, у которых в названии есть 'Lang' и список всех их библиотек")


if __name__ == '__main__':
    main()
