#思路：数组右减左的最大差值
def MAX(A):
    len1 = len(A)
    if len1 < 2:
        return 0
    minPrice = A[0]
    maxPrice = A[1] - A[0]

    for i in range(2, len1):
        if A[i - 1] < minPrice:
            minPrice = A[i - 1]
        Diff = A[i] - minPrice
        if Diff > maxPrice:
            maxPrice = Diff
    if maxPrice < 0:
        maxPrice = 0
    return maxPrice
A = list(map(int,input().split()))
print(MAX(A))