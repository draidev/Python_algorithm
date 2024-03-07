import sys
input = sys.stdin.readline

# 선택 정렬
# 
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[max_idx] > arr[j]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == '__main__':
    N = int(input())
    
    arr = [int(input()) for _ in range(N)]

    # result = selection_sort(arr)
    result = bubble_sort(arr)

    for r in result:
        print(r)