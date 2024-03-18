import sys
input = sys.stdin.readline

# 선택 정렬
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[max_idx] > arr[j]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr

# 버블 정렬
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# 퀵 정렬
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
        return arr
        
if __name__ == '__main__':
    N = int(input())
    
    arr = [int(input()) for _ in range(N)]

    # result = selection_sort(arr)
    # result = bubble_sort(arr)
    # result = quick_sort(arr)
    result = merge_sort(arr)

    for r in result:
        print(r)