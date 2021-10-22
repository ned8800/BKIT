from random import randint

def gen_random(num_count, begin, end):
    n = 0
    while True:
        if n < num_count:
            n += 1
            yield randint(begin, end)
        else:
            break

if __name__ == '__main__':

    a = gen_random(5, 1, 3)
    while True:
        try:
            print(next(a), end=' ')
        except StopIteration:
            print()
            break

