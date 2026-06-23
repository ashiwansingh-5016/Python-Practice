"""Example 1:
Input:
 N = 6, array[] = {9, -3, 3, -1, 6, -5}  
Result:
 5  
Explanation:
 The following subarrays sum to zero:
- {-3, 3}
- {-1, 6, -5}
- {-3, 3, -1, 6, -5}
The length of the longest subarray with sum zero is 5.

Example 2:
Input:
 N = 8, array[] = {6, -2, 2, -8, 1, 7, 4, -10}  
Result:
 8  
Explanation:
 Subarrays with sum zero:
- {-2, 2}
- {-8, 1, 7}
- {-2, 2, -8, 1, 7}
- {6, -2, 2, -8, 1, 7, 4, -10}
The length of the longest subarray with sum zero is 8."""


#Brut Force Approch 


nums = [9, -3, 3, -1, 6, -5]

ans = 0
for i in range(len(nums)):
    sumi = 0 
    for j in range(i , len(nums)):
        sumi += nums[j]
        if sumi == 0:
            ans = max(ans , j-i+1)

print(ans)

# Hasmapping 



nums = [9, -3, 3, -1, 6, -5]
dic = {}
sumi = 0
ans = 0



for i in range(len(nums)):
    sumi += nums[i]

    if sumi ==0:
        ans = i+1




    else:
        if sumi in dic:
            ans = max(ans , i - dic[sumi])


        else:
            dic[sumi] = i
print(ans)




















