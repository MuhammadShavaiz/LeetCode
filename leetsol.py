from collections import defaultdict
from typing import List
import re

"""
Contains Duplicate:
Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

"""
Valid Anagram:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for i in s:
            seen[i] += 1
        for j in t:
            seen[j] -= 1
        for val in seen.values():
            if val != 0:
                return False
        return True

"""
Two Sum:
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target. You may assume that each input would have exactly one solution,
 and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen and seen[complement] != i:
                return [i, seen[complement]]

"""
Valid Palindrome:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        rev_s = s[::-1]
        if s == rev_s:
            return True
        else:
            return False

"""
Best Time to Buy and Sell Stock:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid. An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
"""
class Solution:
    def isvalid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stk.append(i)
            else:
                if len(stk) == 0 or \
                        (i == ")" and stk.pop() != "(") or \
                        (i == "}" and stk.pop() != "{") or \
                        (i == "]" and stk.pop() != "["):
                    return False
        return not stk