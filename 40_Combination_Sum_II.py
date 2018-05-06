'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations


Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8.
Output: 
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5.
Output: 
A solution set is:
[
  [1,2,2],
  [5]
]

'''

import sys, optparse, os

class Solution(object):
    def combinationSum2(self, candidates, target):
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
            
        tuple_output = [tuple(answer) for answer in self.output]
        unique_output = set(tuple_output)
        self.output = [list(answer) for answer in unique_output]

        return self.output

    def combinationSum_DFS(self, candidates, target, sub_output):
        for i in range(len(candidates)):
            if target < candidates[i]:
                break
            elif target == candidates[i]:
                self.output.append(sub_output + [candidates[i]])
                break
            else: # target > candidates[i]
                self.combinationSum_DFS(candidates[i+1:], target - candidates[i], sub_output + [candidates[i]])


candidates = [10,1,2,7,6,1,5]
target = 8

solution = Solution()
result = solution.combinationSum2(candidates, target)
print result
# [[1,1,6],[1,2,5],[1,7],[2,6]]


'''
Complexity Analysis
Time complexity : O(|V|+|E|).
    Depth first search.

Space complexity : O(|V|+|E|).
'''
