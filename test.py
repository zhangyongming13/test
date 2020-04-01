def my_test(elems):
    elems = elems.split(' ')[::-1]
    print(' '.join(elems))


def my_test_1(elems):
    tmp = []
    for i in elems[::-1]:
        if i == ' ':
            print(''.join(tmp[::-1]), end=' ')
            tmp = []
        else:
            tmp.append(i)
    print(''.join(tmp))


if __name__ == '__main__':
    test = 'I want to be a Huawei engineer'
    my_test(test)
    my_test_1(test)
