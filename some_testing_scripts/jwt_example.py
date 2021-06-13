from jwt import encode


################################ Generating some jwt algo ############################################33

def generate_cde(payload, algorithm='HS256'):
    some_jwt = encode({'some': payload}, 'secret', algorithm)
    return some_jwt


def decode(a):
    """
    This function is to decode the jwt code of a user
    :param a:
    :return:
    """
    return decode(a)


if __name__ == '__main__':
    a = generate_cde('payload',algorithm='HS256')
    print(a)
