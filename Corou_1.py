from inspect import getgeneratorstate
# In this Script we use a simple coroutine.
# Here is a very simple Coroutine.
from itertools import count

# Here we can:
# from inspect import getgeneratorstate as gt


def simple_Coroutine():
    print('-> Coroutine started')
    x = yield
    print('-> Coroutine received')


# In this function is a little more complex Coroutine.
def Second_Coroutine(a):
    print('--> Starting: a:', a)
    b = yield a
    print('--> Receiving: b:', b)
    c = yield a + b
    print('--> Receiving c:', c)
