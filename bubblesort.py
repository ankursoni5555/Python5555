def bubblesort(A):
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j + 1], A[j] = A[j], A[j + 1]

    return A


A = [4, 2, 6, 76, 4, 9, 10]
bubblesort(A)
print(A)


