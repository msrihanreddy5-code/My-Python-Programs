import numpy as np

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter Matrix A:")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter Matrix B:")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

C = A + B

print("Sum matrix:")
print(C)
