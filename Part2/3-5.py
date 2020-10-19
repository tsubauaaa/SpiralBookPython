def bubble_sort(A, N):
    flag = True
    i = 0
    while flag:
        flag = False
        for j in reversed(range(N)):
            if j == i:
                break
            if A[j][1] < A[j - 1][1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                flag = True
        i += 1
    return A


def selection_sort(A, N):
    for i in range(N - 1):
        minj = i
        for j in range(i, N):
            if A[j][1] < A[minj][1]:
                minj = j
        A[i], A[minj] = A[minj], A[i]
    return A


N = int(input())
A = input().split()

A_bub = A[:]
A_bub = bubble_sort(A_bub, N)
A_sel = selection_sort(A, N)

print(*A_bub)
print("Stable")
print(*A_sel)
print("Stable" if A_bub == A_sel else "Not stable")
