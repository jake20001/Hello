def gupiao(prices):
    zhuanqian = []
    if len(prices)<=1:
        return 0
    else:
        for j in range(len(prices)):
            for i in range(j+1,len(prices)):
                jiage = prices[i]- prices[j]
                zhuanqian.append(jiage + gupiao(prices[i+1:]))
        return max(zhuanqian)

print(gupiao([7,1,5,3,6,4]))