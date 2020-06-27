import speedtest

"""
Here we can call the next functions in a high level
"""


def some_ex(funct):
    if funct is not None:
        return funct()


def calling_the_fun():
    a = speedtest.main;
    some_ex(a)


if __name__ == '__main__':
    calling_the_fun()
