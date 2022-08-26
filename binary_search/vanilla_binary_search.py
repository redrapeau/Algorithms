from typing import List

def binary_search(arr: List[int], target: int) -> int:
    left_idx, right_idx = 0, len(arr)-1
    
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx)//2
        
        if arr[mid_idx] == target:
            return mid_idx
        elif arr[mid_idx] < target:
            left_idx = mid_idx + 1
        elif arr[mid_idx] > target:
            right_idx = mid_idx - 1

    return -1

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)



# first try:
#def binary_search(arr: List[int], target: int) -> int:
    # left_idx, right_idx = 0, len(arr)-1
    # mid_idx = (left_idx + right_idx)//2
    
    # while arr[mid_idx] != target:
    #     mid_idx = (left_idx + right_idx)//2
        
    #     if arr[mid_idx] < target:
    #         left_idx = mid_idx + 1
    #     elif arr[mid_idx] > target:
    #         right_idx = mid_idx - 1
    
    #     if left_idx > right_idx:
    #         return -1
    # return mid_idx