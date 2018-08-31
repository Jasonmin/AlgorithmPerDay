
# binary_search

def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)/2
        print('==>')
        print(mid)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None

my_list = [1,3,5,6,7,9,11,14,16,18,21,29,30,31,33,36,41,45,47,49,50,51,52,55,58,59,60]

print binary_search(my_list,3)
# print binary_search(my_list,10)
