import math

def pow(x, y):
    return x ** y

float_answer = math.pow(2, 4)

x, y = [3, 3], [6, 12]
def euclidean_dist(x, y):
    inside = pow((x[0] - y[0]), 2) + pow((x[1] - y[1]), 2)
    euc = pow(inside, 0.5)
    math_euc = math.dist(x, y)
    return {"euclidean": euc, "math library euclidean": math_euc}

print(euclidean_dist(x, y))

print(int(float_answer)) # 16
print(pow(3, 5)) # 243