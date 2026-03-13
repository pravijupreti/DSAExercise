import random
import time

# 1. Create data structure with at least 300 elements
data = [random.randint(1, 1000) for _ in range(300)]


# -------------------------
# Quick Sort
# -------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


# -------------------------
# Merge Sort
# -------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# -------------------------
# Insertion Sort
# -------------------------
def insertion_sort(arr):
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


# -------------------------
# Measure performance
# -------------------------

# Quick Sort
start = time.time()
sorted_quick = quick_sort(data.copy())
end = time.time()
print("Quick Sort Time:", end - start)
print("Sorted Data (Quick Sort):", sorted_quick)


# Merge Sort
start = time.time()
sorted_merge = merge_sort(data.copy())
end = time.time()
print("\nMerge Sort Time:", end - start)
print("Sorted Data (Merge Sort):", sorted_merge)


# Insertion Sort
start = time.time()
sorted_insertion = insertion_sort(data.copy())
end = time.time()
print("\nInsertion Sort Time:", end - start)
print("Sorted Data (Insertion Sort):", sorted_insertion)