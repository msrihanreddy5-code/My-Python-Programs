print("Enter your choice: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Transpose")
choice = int(input("Enter your choice(1-4): "))
if choice ==1:
    r=int(input("Enter number of rows: "))
    c=int(input("Enter number of columns: "))
    print("Enter the first matrix: ")
    matrix1 = []
    for i in range(r):
        row = list(map(int, input().split()))
        matrix1.append(row)
    print("Enter the second matrix: ")
    matrix2 = []
    for i in range(r):
        row = list(map(int, input().split()))
        matrix2.append(row)
    result = []
    for i in range(r):
        result_row = []
        for j in range(c):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(result_row)
    print("Result of addition: ")
    for row in result:
        print(row)
elif choice == 2:
    r=int(input("Enter number of rows: "))
    c=int(input("Enter number of columns: "))
    print("Enter the first matrix: ")
    matrix1 = []
    for i in range(r):
        row = list(map(int, input().split()))
        matrix1.append(row)
    print("Enter the second matrix: ")
    matrix2 = []
    for i in range(r):
        row = list(map(int, input().split()))
        matrix2.append(row)
    result = []
    for i in range(r):
        result_row = []
        for j in range(c):
            result_row.append(matrix1[i][j] - matrix2[i][j])
        result.append(result_row)
    print("Result of subtraction: ")
    for row in result:
        print(row)
elif choice == 3:
    r1=int(input("Enter number of rows for first matrix: "))
    c1=int(input("Enter number of columns for first matrix: "))
    print("Enter the first matrix: ")
    matrix1 = []
    for i in range(r1):
        row = list(map(int, input().split()))
        matrix1.append(row)
    r2=int(input("Enter number of rows for second matrix: "))
    c2=int(input("Enter number of columns for second matrix: "))
    print("Enter the second matrix: ")
    matrix2 = []
    for i in range(r2):
        row = list(map(int, input().split()))
        matrix2.append(row)
    if c1 != r2:
        print("Error: Number of columns in first matrix must be equal to number of rows in second matrix.")
    else:
        result = []
        for i in range(r1):
            result_row = []
            for j in range(c2):
                sum_product = 0
                for k in range(c1):
                    sum_product += matrix1[i][k] * matrix2[k][j]
                result_row.append(sum_product)
            result.append(result_row)
        print("Result of multiplication: ")
        for row in result:
            print(row)
elif choice == 4:
    r=int(input("Enter number of rows: "))
    c=int(input("Enter number of columns: "))
    print("Enter the matrix: ")
    matrix = []
    for i in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)
    result = []
    for j in range(c):
        result_row = []
        for i in range(r):
            result_row.append(matrix[i][j])
        result.append(result_row)
    print("Result of transpose: ")
    for row in result:
        print(row)
else:
    print("Invalid choice! Please enter a number between 1 and 4.")
print("Thank you for using the matrix calculator!")
