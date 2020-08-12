'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

## UPER



def single_number(arr):
    # Your code here
    ## counter to keep track of position
    ## loop through 
        ## compare i to i +1
        ## if equal add 2 to count
        ## if not equal return count

    counter = 0    
    # for _ in range(0, len(arr)):
    #     if arr[counter] == arr[counter + 1]:
    #         counter += 2
    #     else:
    #         return arr[counter]


    arr.sort() ## sort array
    for _ in range(0, len(arr) - 1): ## loop through array
        if counter >= len(arr): ## if counter is greater than length return last element
            return arr[-1]
        elif arr[counter] == arr[counter + 1]: ## if counter and counter+1 are eqal add 2 to tje counter
            counter += 2
        else:
            return arr[counter] ## if counter and counter+1 are not equal return counter
            

            




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1,99, 1, 4, 4, 7, 5, 5, 3, 12, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")