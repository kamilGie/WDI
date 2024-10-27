# Zadanie 17.
# Napisać program wyliczający pierwiastek równania x^x = 2020 metodą stycznych.


import math


def solve(f, df):
    x = 1
    eps = 0.0001
    prev_x = x + eps * 10
    while abs(prev_x - x) > eps:
    #for i in range(1000):
        prev_x = x
        x = x - f(x)/df(x)

    print(x)



def function(x):
    return x**x - 2020

def derivative(x):
    return (x**x)*(math.log(x)+1)

# OR 

def log_function(x):
    return x*math.log(x) - math.log(2020)

def log_derivative(x):
    return math.log(x) + 1


if __name__ == "__main__":
    solve(log_function, log_derivative)
