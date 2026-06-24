nums =  [2, 3, 5, -2, 7, -4]  
start = 0
end = -1
maxi = 0 
sumi = 0 
for i in range(len(nums)):
    sumi+=nums[i]

    if maxi < sumi:
        maxi = sumi
        end = i

    if sumi <0:
        sumi = 0
        start = i+1

print(maxi , start , end )