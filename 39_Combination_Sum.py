'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations


Example 1:

Input: candidates = [2,3,6,7], target = 7.
Output: 
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
Output: 
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''

import sys, optparse, os

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        self.target = target
        self.output = []

        if not candidates or target < candidates[0]:
            return []
        else:
            self.combinationSum_DFS(candidates, target, [])

        return self.output

    def combinationSum_DFS(self, candidates, target, sub_output):
        for i in range(len(candidates)):
            if target < candidates[i]:
                break
            elif target == candidates[i]:
                self.output.append(sub_output + [candidates[i]])
                break
            else: # target > candidates[i]
                self.combinationSum_DFS(candidates[i:], target - candidates[i], sub_output + [candidates[i]])


candidates = [8,7,4,3]
target = 11

solution = Solution()
result = solution.combinationSum(candidates, target)
print result
# [[3, 4, 4], [3, 8], [4, 7]]


'''
Complexity Analysis
Time complexity : O(|V|+|E|).
    Depth first search.

Space complexity : O(|V|+|E|).
'''
