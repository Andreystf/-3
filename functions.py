def read_file(text):
    with open(text, 'r') as file:
        a = []
        for i in file.read().split():
            a.append(int(i))
    return a


def maximum(m):
    a = m[0]
    for i in m:
        if i > a:
            a = i
    return a


def minimum(m):
    a = m[0]
    for i in m:
        if i < a:
            a = i
    return a


def suma(m):
    a = 0
    for i in m:
        a += i
    return a


def proizvedenie(m):
    a = 1
    for i in m:
        a *= i
    return a


if __name__ == '__main__':
    print(*read_file('data_file.txt'))
    print(minimum(read_file('data_file.txt')))
    print(maximum(read_file('data_file.txt')))
    print(suma(read_file('data_file.txt')))
    print(proizvedenie(read_file('data_file.txt')))
