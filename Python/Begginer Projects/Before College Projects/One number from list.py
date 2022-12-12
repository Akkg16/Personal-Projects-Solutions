

def GetX(n, nums):
 print(nums[n])

n = int(input("Enter number of elements : ")) 
  
# Below line read inputs from user using map() function  
nums = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
  
print(nums[n])