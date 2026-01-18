import math

def sigmoid(x): return 1/(1+math.exp(-x))

w,b = 0.5,0.1
x = 1
print(sigmoid(w*x+b))
