def input_complex():
    re = int(input("Częszć rzeczywista:"))
    im = int(input("Częszć urojona:"))

    return re, im


def add_complex(c1, c2):
    return c1[0]+c2[0], c1[1]+c2[1]


def multiply_complex(c1, c2):
    return c1[0]*c2[0]+c1[1]*c2[1], c1[0]*c2[1]+c2[0]*c1[1]


def divide_complex(c1, c2):
    ...