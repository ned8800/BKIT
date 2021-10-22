import math

def myprint(x):
    if (x > 0):
        print (f'x = {(-1)*(x**0.5)}')
        print (f'x = {(x**0.5)}')
    elif (x == 0):
        print("x = 0")
    else:
        print ("x - не действительный корень")
    
while True:
    a = str(input("a = "))
    if ((a.isdigit() or (a[0] == str('-'))) and (a[0] != '0')):
        break
    else:
        print("type again")
a = float(a)
    
while True:
    b = str(input("b = "))
    if b.isdigit() or (b[0] == str('-')):
        break
    else:
        print("type again")
b = float(b)

while True:
    c = str(input("c = "))
    if c.isdigit() or (c[0] == str('-')):
        break
    else:
        print("type again")
c = float(c)
while True:
    if a != 0:
        d = b ** 2 - 4*a*c
        if d > 0:
            x1 = (-b - d**0.5) / (2*a)
            x2 = (-b + d**0.5) / (2*a)
            myprint(x1)
            myprint(x2)
            break
        if d == 0:
            x = (-b)/(2*a)
            if (x >= 0):
                myprint(x)
                break
            else:
                print("Нет действительных корней")
                break
        if d < 0:
            print ("Нет действительных корней")
            break
        if a != 0 and b == 0 and c == 0:
            x1 = (-a**0.5)
            x2 = -(-a**0.5)
            print (f'x1 = {x1}')
            print (f'x2 = {x2}')
            break
        if a != 0 and b != 0 and c == 0:
            print ("x1 = 0")
            x2 = (-b/a)
            myprint(x2)
            break
    else:
        print ("Решение сводится к квадратному")
        break
