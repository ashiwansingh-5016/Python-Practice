nums =[7,1,5,3,6,4]
profit = 0 
mini = nums[0]
for num in nums :
    if num < mini :
        mini = num

    #Profit 
    profit = max(profit  ,  num - mini)

print(profit)