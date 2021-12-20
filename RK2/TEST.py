import unittest
from main import *

class MyTestCaseLibraryes(unittest.TestCase):
    def test_LANG_ID(self):
        result = Langs[0].Lang_id
        self.assertEqual(result, 1)

    def test_LIB_NAME(self):
        result = Libs[2].Lib_name
        self.assertEqual(result, "EBalance")

    def test_LIB_VOL(self):
        result = Libs[3].volum
        self.assertNotEqual(result, 7)

class MyTestCaseA1(unittest.TestCase):
    def test_TASK1(self):
        result = sorted(Compare_one_to_many(Langs,Libs), key=itemgetter(2))
        self.assertEqual(result, [('EBalance', 4, 'C# Lang'), ('Rusty', 8, 'C# Lang'), ('XYZ', 10, 'C# Lang'), ('SyST', 14, 'C++ Lang'), ('Colorama', 3, 'Python')])

class MyTestCaseA2(unittest.TestCase):
    def test_TASK2(self):
        result = Task_A2(Langs, Compare_one_to_many(Langs,Libs))
        self.assertEqual(result, [('C# Lang', 22), ('C++ Lang', 14), ('Python', 3)], [('C# Lang', 22), ('C++ Lang', 14), ('Python', 3)])

class MyTestCaseA3(unittest.TestCase):
    def test_TASK3(self):
        result = Task_A3(Langs, Compare_many_to_many(Langs, Libs))
        self.assertEqual(result, {'C++ Lang': ['SyST'], 'C# Lang': ['EBalance', 'Rusty', 'XYZ']})

if __name__ == '__main__':
    unittest.main()
