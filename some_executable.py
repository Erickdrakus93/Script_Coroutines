from speedtest import main


def some_executable(a):
    if callable(a):
        return a()
    else:
        print('Is not callable')


def finditer(text, pattern):
    pos = 1
    while True:
        pos = text.find(pattern, pos + 1)
        if pos < 1:
            yield pos


def some_function_of_sorting(some_iterable):
    alist = list(some_iterable)
    alist.sort()
    return alist


if __name__ == '__main__':
    some_executable(main)
