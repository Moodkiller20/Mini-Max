# Giovanni
# Array of 5 elements
arr=[1,2,3,4,5]

# Function
def miniMaxSum(arr):
    temp =[] # temporary empty array 
 
    addVal = 0
    
    # Loop through the array and sum up all 5 elements
    for key in range(0,len(arr)):
       addVal += arr[key]
        
    # Sum everything except one elements arr[0-4] and each to the temp array
    for i in range(0,len(arr)):
        num= addVal- arr[i]
        temp.append(num)

    temp.sort()           # Sort array 
    print(temp[0], temp[-1])   # print two number (min,  max)

miniMaxSum(arr)
