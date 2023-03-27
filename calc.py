def add(x, y):
    '''Add Function'''
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    if y == 0:
        raise ValueError('Can not devide by zero!')
    return x / y
