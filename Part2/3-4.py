def selection_sort(A, N):
    sw = 0
    for i in range(N - 1):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        A[i], A[minj] = A[minj], A[i]
        if i != minj:
            sw += 1

    return A, sw


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    A, sw = selection_sort(A, N)
    print(*A)
    print(sw)
