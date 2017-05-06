
def summa (arr):
    if arr == []:
        return 0
    else:
        return arr[0] + summa(arr[1:])

def count_el (arr):
    if arr == []:
        return 0
    else:
        return 1 + count_el(arr[1:])

def find_max (arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    submax = find_max(arr[1:])
    return arr[0] if arr[0] > submax else submax

def quicksort (arr):
    if len(arr) < 2:
        return arr
    else:
        found = arr[0]
        less = [i for i in arr[1:] if i <= found]
        greater = [i for i in arr[1:] if i > found]
    return quicksort(less) + [found] + quicksort(greater)


a = [8, 2, 4, 6, 7]

print(summa(a))
print(count_el(a))
print(find_max(a))
print(quicksort(a))