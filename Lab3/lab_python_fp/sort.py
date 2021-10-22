data = [4, -30, 100, -100, 123, 1, 0, -1, -4]


if __name__ == '__main__':
    result = sorted((data.copy()), key=abs, reverse=True)
    print(result)

    result_with_lambda = (lambda x: sorted((x), key=abs, reverse=True))(data.copy())
    print(result_with_lambda)

