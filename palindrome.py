# number = int(input("Enter a number for Check palindrom or Not : "))
# temp=number
# rev = 0
# while number > 0:
#     last = number % 10 #last number we taken
#     number= number//10 #last number we remove in original number
#     rev = (rev*10)+last
# print(rev)
# if temp == rev:
#     print("it is a palindrome number")
# else:
#     print("it is not a palindrome ")
#
# """palindriome words"""
#
#
# string = input("Enter a check palindrom : ")
# rev = ""
# for i in range(len(string)- 1,-1,-1):
#     rev = rev + string[i]
# print(rev)
#
# if string == rev:
#     print("it is a palindrome")
# else:
#     print("not a palindromr")
class Solution:
    def duplicates(self, arr, n):
        seen = []
        duplicate = []
        for i in arr:
            if i in seen:
                duplicate.append(i)
            else:
                seen.append(i)
        if duplicate:
            res = list(duplicate)
            return (res)
        else:
            return [-1]


# {
# Driver Code Starts
if (__name__ == '__main__'):
    t = int(input("Enter a t : "))
    for i in range(t):
        n = int(input("enter a n :"))
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i, end=" ")
        print()

# } Driver Code Ends
print(res)  # Output: [2, 3, 6]