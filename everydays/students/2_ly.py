class Solution(object):

    def __init__(self):
        pass

    def xxx(self,s):
        num = 0
        t = ""
        for i in range(len(s)):
            if s.count(s[i])%2 != 0:
                num += 1
                odd = s[i]
                if num > 1 and odd != t:
                    return False
                t =odd
        return len(s)


    def longestAwesome(self, s) :
        max_len = 1
        n = len(s)
        for i in range(n-1):
            for j in range(i+2,n+1):
                max_len = max(max_len,self.xxx(s[i:j]))
        return max_len


mSolution = Solution()
print(mSolution.longestAwesome('5223253960474154783'))
