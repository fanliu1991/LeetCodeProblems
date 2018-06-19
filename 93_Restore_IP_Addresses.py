'''
Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

'''

import sys, optparse, os

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        """
        Depth First Search
        """

        def dfs(current_s, part_index, current_path):
            if part_index == 4:
                if current_s == "":
                    result.append(current_path[:-1])
                else:
                    return
            else:
                for digits in range(1, 4):
                    if digits <= len(current_s):
                        if digits == 1:
                            dfs(current_s[1:], part_index+1, current_path + current_s[:1] + ".")
                        else:
                            if current_s[0] != "0" and int(current_s[:digits]) <= 255:
                                dfs(current_s[digits:], part_index+1, current_path + current_s[:digits] + ".")

        result = []
        part = 0
        path = ""
        dfs(s, part, path)
        return result

        # result = []
        # for a in range(1, 4):
        #     for b in range(1, 4):
        #         for c in range(1, 4):
        #             for d in range(1, 4):
        #                 if a+b+c+d == len(s):
        #                     A = int(s[:a])
        #                     B = int(s[a:a+b])
        #                     C = int(s[a+b:a+b+c])
        #                     D = int(s[a+b+c:a+b+c+d])
        #                     if A <= 255 and B <= 255 and C <= 255 and D <= 255:
        #                         ip_address = str(A) + "." + str(B) + "." + str(C) + "." + str(D)
        #                         if len(ip_address) == len(s)+3: # in case of ip_address = 0.12.00.000
        #                             result.append(ip_address)
        # return result


s = "25525511135"

solution = Solution()
result = solution.restoreIpAddresses(s)
print result


'''
Complexity Analysis
Time complexity : O(3^n).
    DFS algorithm, at every node there are 3 possible sub paths.

Space complexity : O(3^n).
    Extra space is used to store split nodes.
'''

