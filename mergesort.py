def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)


def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle + 1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    L = A[first:middle + 1]
    R = A[middle + 1:last + 1]

    L.append(9999999)
    R.append(9999999)

    i = j = 0

    for k in range(first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1

        else:
            A[k] = R[j]
            j = j + 1


A = [1, 4, 3, 6, 3, 23, 4, 5, 7, 9, 11, 22, 45, 66, 45, 34, 89, 11, -1]
merge_sort(A)
print(A)

# Best Method Complexity is = n x (log n)