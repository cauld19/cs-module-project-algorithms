'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    ## with division
    ## loop through all elements multiplying
    
    ## loop again dividing by element at location arr[i]
        ## append this to new arr and return
        
    ## return newarr
    newarr = []
    curr = 1
    
    for i in range(0, len(arr)):
        curr *= arr[i] 
    for i in range(0, len(arr)):
        newarr.append(curr // arr[i])

    return newarr

    




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
