import sys
import jwt



class Singleton(object):
    _singletons = {}
    """
    .. code::
    This method is to generate the pattern of the code as the main manner to 
    call inside of the main function as we can see
    This is to use and generates the manner to call inside of the main function
    
    """

    def __new__(cls, *args, **kwargs):
        if cls not in cls._singletons:
            cls._singletons[cls] = super(Singleton, cls).__new__(cls)
        return cls._singletons[cls]


def generate_the_token(key):
    """
    ´input': key as private key

    """
    token_str = jwt.decode({'some_payload': 'payload'}, key, algorithm='HS256')
    return token_str.decode('utf-8')
