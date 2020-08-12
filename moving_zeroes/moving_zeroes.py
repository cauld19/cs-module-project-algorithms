'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    ## create new array to reorder ele to
    ## if ele in array is not 0 append to new arr
    ## if ele is 0 insert at end of newarr
    
    ## or
    
    ## create array of non zero numbers
    ## create array of zeros
    ## extend array of zeros to end of non zeros array
    newarr = []
    newarr2 = []

    for i in range(0, len(arr)):
        if arr[i] != 0:
            newarr.append(arr[i])
        else:
            newarr2.append(arr[i])
            
    newarr.extend(newarr2)

    # for j in range(0, len(arr)):
    #     if arr[j] == 0:
    #         newarr.insert(len(arr), arr[j])

    

    return newarr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")