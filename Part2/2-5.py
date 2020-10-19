n = int(input())
R = [int(input()) for _ in range(n)]

max_benefit = -2 * 10 ** 18
min_R = R[0]

for i in range(1, n):
    max_benefit = max(max_benefit, R[i] - min_R)
    min_R = min(min_R, R[i])

print(max_benefit)
