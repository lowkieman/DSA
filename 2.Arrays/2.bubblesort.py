#bubble sort is an algorithm that sorts an array from the lowest value
#to the highest value
nums=[20,58,6,70,88,10,34,65,76,78,7,76];
n=len(nums);
for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            swapped=True;
        if not swapped:
            break
print("sorted array: ",nums)