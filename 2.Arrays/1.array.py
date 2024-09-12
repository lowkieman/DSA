nums=[7,8,29,58,20,6,2,3,4,5,1]

minNum=nums[0];

for i in nums:
    if i<minNum:
        minNum=i;

print("lowest Value: ",minNum)