from scipydirect import minimize


def obj(x):
    """Six-hump camelback function"""
    x1 = x[0]
    x2 = x[1]
    f = (4 - 2.1*(x1*x1) + (x1*x1*x1*x1)/3.0)*(x1*x1) + x1*x2 + (-4 + 4*(x2*x2))*(x2*x2)
    return f


bounds = [(-3, 3), (-2, 2)]

res = minimize(obj, bounds)

print(res)