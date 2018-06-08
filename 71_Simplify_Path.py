'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

1. Did you consider the case where path = "/../"?
    In this case, you should return "/".

2. Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".

'''

import sys, optparse, os

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        '''
        "/b/c/" : directory 'b ' -> directory 'c '
        "." : current directory
        "./" : current directory
        "../" : one directory up

        e.g
        "/" : root directory
        "b/c/../" : it will go from c to b
        "c/b/./" : it is still in directory b

        '''

        paths = [p for p in path.split("/") if p != "." and p != ""]
        stack = []

        for p in paths:
            if p != "..":
                stack.append(p)
            else:
                if len(stack) > 0:
                    stack.pop()

        return "/" + "/".join(stack)


path = "//home/a/./b/../../c/"

solution = Solution()
result = solution.simplifyPath(path)
print result

'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the path array.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
