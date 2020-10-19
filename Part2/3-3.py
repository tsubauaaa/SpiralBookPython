def bubble_sort(A, N):
    sw = 0
    flag = True
    i = 0
    while flag:
        flag = False
        for j in reversed(range(N)):
            if j == i:
                break
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                flag = True
                sw += 1
        i += 1
    return A, sw


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    A, sw = bubble_sort(A, N)

    print(*A)
    print(sw)
