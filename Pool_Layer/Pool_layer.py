class ReusablePool(object):
    """
    Manage Reusable objects for use by client Objects
    """

    def __init__(self, size):
        self._reusables = [Reusable() for _ in size]  # This is the collections as we can see

    def aquire(self):
        return self._reusables.pop()

    def relese(self, reusable):
        self._reusables.append(reusable)


class Reusable(object):
    """
    Collaborate with Other Object for a limited amount of the time,
    then they are no longer needed for that collaboration
    """
    pass


"""
Here we can define the test function
"""


def func_test():
    reusable_pool = ReusablePool(55)
    reusable_resource = reusable_pool.aquire()
    reusable_pool.relese(reusable_resource)


if __name__ == '__main__':
    func_test()
