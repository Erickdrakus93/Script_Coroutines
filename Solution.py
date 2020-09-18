import sys


def list_len(L, i, v=None):
    """This is the use of the next solutions as we can see  """
    if -len(L) <= i <= len(L):
        return L[i]
    else:
        return v


def list_the_index(list, i, v=None):
    """This function is to use it as a reference of the main objects"""
    try:
        return list[i]
    except IndexError as e:
        return v


if __name__ == '__main__':
    L = [1, 2, 3, 4, 443]
    list_len(L, 1, v=1)
