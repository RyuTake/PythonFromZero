import numpy as np
x = np.array([0, 1])
b = -0.7
w = np.array([0.5, 0.5])

multiple = w*x
npSum = np.sum(w*x)
npSumBias = np.sum(w*x)+b

print(multiple)
print(npSum)
print(npSumBias)