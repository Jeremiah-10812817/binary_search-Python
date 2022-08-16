# A simple binary search algorithm
arr=[0,1,2,3,4,5,6,8,9,10]

def binary_search(arr, searchKey):
    begin=0
    ending=len(arr)
    midpoint=0
    value_at_midpoint=0

    while begin<=ending:
        midpoint=int((begin+ending)/2)
        value_at_midpoint=arr[midpoint]
        if value_at_midpoint< searchKey:
            ending=midpoint
        elif value_at_midpoint> searchKey:
            begin=midpoint
        elif value_at_midpoint==searchKey:
            return midpoint

a=(binary_search(arr,5))   
print ('Search Key is at index', a)
        



