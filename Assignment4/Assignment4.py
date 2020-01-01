import math as m


def signoid(z):
    return 1 / (1 + m.pow(m.e, -z))


def tanh(z):
    return (m.pow(m.e, z) - m.pow(m.e, -z)) / (m.pow(m.e, z) + m.pow(m.e, -z))


def relu(z):
    if z < 0:
        return 0
    if z > 1:
        return 1
    return z


def leaky_relu(z):
    if z < 0:
        return z * 0.005
    if z > 1:
        return 1
    return z


def parameterized_relu(z, p):
    if z < 0:
        return p * z
    if z > 1:
        return 1
    return z


def softmax(z, t):
    if z < t:
        return 0
    else:
        return 1


def swish(z):
    return z / (1 + m.pow(m.e, -z))


print(signoid(12))
print(tanh(12))
print(relu(12))
print(leaky_relu(12))
print(parameterized_relu(12, 0.9))
print(softmax(12, 9))
print(swish(12))
