n = int(input())
arr = list(map(int, input().split()))

def partition(arr, low, high):
    p_idx = select_pivot(arr, low, high)
    arr[p_idx], arr[high] = arr[high], arr[p_idx]
    i = low - 1

    for j in range(low, high):
        if arr[j] < arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]    
    return i + 1

def select_pivot(arr, low, high):
    mid = (low + high) // 2

    if arr[low] >= arr[high]:
        if arr[low] <= arr[mid]:
            return low
        if arr[mid] >= arr[high]:
            return mid
        return high
    else:
        if arr[high] <= arr[mid]:
            return high
        if arr[mid] >= arr[low]:
            return mid
        return low

def quick_sort(arr, low, high):
    if low < high:
        pos = partition(arr, low, high)

        quick_sort(arr, low, pos - 1)
        quick_sort(arr, pos + 1, high)

quick_sort(arr, 0, n - 1)
print(*(arr))