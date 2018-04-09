
import sys, optparse, os

class Solution:
    def test(self, a, b):

        if a == True and b == True:
            return True
        else:
            print "condition 2"
            return False


a = True
b = False

solution = Solution()
indices = solution.test(a, b)
print indices

'''
                        lowest to highest precedence:
                            Lambda  #运算优先级最低
                            逻辑运算符: or
                            逻辑运算符: and
                            逻辑运算符:not
                            成员测试: in, not in
                            同一性测试: is, is not
                            比较: <,<=,>,>=,!=,==
                            按位或: |
                            按位异或: ^
                            按位与: &
                            移位: << ,>>
                            加法与减法: + ,-
                            乘法、除法与取余: *, / ,%
                            正负号: +x,-x
                        '''