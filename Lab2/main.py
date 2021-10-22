from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.rectangle import Rectangle
from colorama import *

def main():
    n = int(input("n = "))
    r = Rectangle("синего", n, n)
    c = Circle("зеленого", n)
    s = Square("красного", n)
    print(r)
    print(c)
    print(s)
    print(Fore.BLUE + 'some Blue text')


if __name__ == "__main__":
    main()
