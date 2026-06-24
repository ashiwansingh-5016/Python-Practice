nums = [-1,0,1,2,-1,-4]
ans = []
for i in range(len(nums)):
    for j in range(i+1 ,len(nums)):
        for k in range(j+1 ,len(nums)):
            if ( i!=j!=k) and (nums[i] + nums[j] + nums[k] == 0):
                ls = [nums[i] ,nums[j] , nums[k]]
                ans.append(ls)
print(ans)