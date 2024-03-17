def solution(numbers):
    # Convert integers to strings
    numbers = [str(num) for num in numbers]
    
    # Define custom sorting function
    def custom_sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]
        left = [x for x in arr[1:] if int(x + pivot) >= int(pivot + x)]
        right = [x for x in arr[1:] if int(x + pivot) < int(pivot + x)]
        
        return custom_sort(left) + [pivot] + custom_sort(right)
    
    # Sort the array using the custom sorting function
    sorted_numbers = custom_sort(numbers)
    
    # Concatenate sorted strings into a single string
    result = ''.join(sorted_numbers)
    
    return result