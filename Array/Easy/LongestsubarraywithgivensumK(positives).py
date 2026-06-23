"""Example 1:
Input:
 nums = [10, 5, 2, 7, 1, 9], k = 15  
Output:
 4  
Explanation:
 The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

Example 2:
Input:
 nums = [-3, 2, 1], k = 6  
Output:
 0  
Explanation:
 There is no sub-array in the array that sums to 6. Therefore, the output is 0."""



# Brute Force Method 



nums =  [10, 5, 2, 7, 1, 9]
k = 15  
n = len(nums)

maxicount = 0 
for i in range(n):
    sums = 0
    for j in range(i , n):
        sums+= nums[j]

        if sums ==k :
            length = j-i+1
            maxicount = max(maxicount , length)

print(maxicount)



#Optimal Approch







prefix_sum = 0
max_len = 0

# prefix_sum : first index where it appeared
mp = {0: -1}

for i, num in enumerate(nums):
    prefix_sum += num

    if prefix_sum - k in mp:
        length = i - mp[prefix_sum - k]
        max_len = max(max_len, length)

    if prefix_sum not in mp:
        mp[prefix_sum] = i

print(max_len)




##### Trying myself 



#Brut Forcce 



Ans = 0

for i in range(len(nums)):
    length =0 
    asf = 0 
    for j in range(i,len(nums)):
        asf += nums[j]
        length +=1
        if asf == k:
            Ans = max(Ans , length)

print(Ans)








# Sliding Window // Two Pointer Concept 

n = len(nums)

left = 0
right = 0
sumi = nums[0]
validAnswer = 0
while right <= n:

    while left <= right and sumi >k:
        sumi -= nums[left]
        left +=1
    
    if sumi == k:
        validAnswer = max(validAnswer , right -left +1)

    right +=1
    if right < n:
        sumi += nums[right]

print(validAnswer)




















