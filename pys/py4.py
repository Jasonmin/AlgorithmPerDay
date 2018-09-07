
def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less = [i for i in array[1:] if i<=pivot]
        greater = [i for i in array[1:] if i>pivot]

        return quicksort(less)+[pivot]+quicksort(greater)

print quicksort([2,3,5,66,7,8,1,2,7,3,5,78,43,11,33,55,745,145])

