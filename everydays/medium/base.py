#coding=utf-8
a = [10,1,-3,4,-1,2,0,-5,4]
def func():
    #找最大子序和结尾index
    b= a.copy()
    for i in range(1,len(b)):
        if b[i-1] > 0:
            b[i] += b[i - 1]
    max_index = b.index(max(b))
    print("max value:",max(b))
    print("max index:",max_index)

    #找最大子序和起始index
    c= a.copy()
    if max(b)>0:
        min_index = 0
        for i in range(len(a)):
            c[max_index] += c[max_index -i-1]
            max_sum = c[max_index]
            if max_sum == max(b):
                min_index = c.index(c[max_index -i-1])
                print("min index:",min_index)
                break
    else:
        min_index = max_index
    return a[min_index:max_index+1]
mx = func()
print("reslut:",mx)