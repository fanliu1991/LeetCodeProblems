'''
Given a string s, 
partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output: 
[
    ["aa","b"],
    ["a","a","b"]
]
'''

import sys, optparse, os

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        if not s:
            return []
        
        result = []
        
        def dfs(rest_s, current_partition):
            if not rest_s:
                nonlocal result
                result.append(current_partition)
            
            for i in range(1, len(rest_s)+1):
                substring = rest_s[:i]
                if substring == substring[::-1]: # chech isPalindrome
                    dfs(rest_s[i:], current_partition + [substring])
            return

        dfs(s, [])

        return result


s = "aab"

solution = Solution()
result = solution.partition(s)
print result

'''
Complexity Analysis
Time complexity: O(n*2^n), where n is the length of s.
    In the worst case (e.g. "aa...aa"), there are O(2^n) kind of partition configuration, 
    and each configuration takes O(n) to check isPalindrome.

Space complexity : O(n).
    Extra space is used to store current_partition of each partition configuration.
'''

