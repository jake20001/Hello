# 求数组中连续多个元素和最大的组合

def fmax2(a):
    max = 0
    for i in range(2, len(a)+1):  # 连续求和的元素个数
        for j in range(0, len(a)-i+1):  # 元素求和的起始下标
            sum = 0  # 存储每次元素相加的和，循环开始时重置为0
            for k in range(j, j+i):  # 元素求和，下限为求和起始元素下标，上限为求和末尾元素下标
                sum += a[k]
            if sum > max:
                max = sum
                index = [j, j+i-1]  # 每次记录求和值更大的一组的起始下标和末尾下标
    return index, max  # 返回元素组合和最大值


a = [10, -3, 4, -2, 5, -1, 6]
print(fmax2(a))
