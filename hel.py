# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#         return []
# s1=Solution()
# a=s1.twoSum([7,2,11,15],18)
# print(a)
# # class Solution:
# #     def twoSum(self, nums, target):
# #         n = len(nums)
# #         for i in range(n - 1):
# #             for j in range(i + 1, n):
# #                 if nums[i] + nums[j] == target:
# #                     return [nums[i], nums[j]]
# #         return []  # No solution found
# # s1=Solution()
# # print(s1.twoSum([2,7,11,15],9))

row = int(input("Enter a number for Row : "))
for i in range(row):
    for j in range(row-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()