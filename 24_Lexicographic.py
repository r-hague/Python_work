p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def next_perm(arr):
    #find non-increasing suffix
    i = len(arr)-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    #find successor to pivot
    j = len(arr)-1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]

    #reverse suffix
    arr[i:] = arr[len(arr) - 1 : i - 1 : -1]
    return arr


for k in range(1, 1000000):
    p = next_perm(p)


print p




