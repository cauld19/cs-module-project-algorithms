'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # set current index
        ##curr index + k, curr index - k
    # compare k to find largest value
    # put value in new array
    # move k over one element and repeaat
    # return newarr when k is at end of arr
    
    newarr = []
    curr = 0
    if k > len(nums):
        return False
    else:
        for i in range(0, len(nums)):
            if curr + k > len(nums):
                return newarr
            else:
                newarr.append(max(nums[curr:curr + k]))
                curr += 1
        return newarr
            
            
        
        


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
