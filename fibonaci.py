num = int(input("Enter a number : "))
n1,n2=0,1
sum = 0
if num <= 0:
    print("please enter a number greater than 0")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1=n2
        n2=sum
        sum=n1+n2
# -------------------
"""Move All Zero to last"""
class Solution:
  num = [0,1,0,4,0,53,0]
  def moveAllZero(self,num:list[int]):
    left = 0 
    for r in range(num):
      if num[r]:
        num[left],num[r] = num[r],num[left]
        left +=1
    return num