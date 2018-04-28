def insertionsort(A):
    for i in range(1, len(A)):
        for j in range(i - 1, -1, -1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
            else:
                break


A = [1, 5, 3, 7, 8, 0, 12]
insertionsort(A)
print(A)


### O(n^2) is the complexity