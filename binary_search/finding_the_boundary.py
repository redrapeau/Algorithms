'''
An array of boolean values is divided into two sections;
the left section consists of all false and the right section consists of all true.
Find the boundary of the right section, i.e. the index of the first true element.
If there is no true element, return -1.

Input: arr = [false, false, true, true, true]

Output: 2

Explanation: first true's index is 2.
'''

from typing import List

def find_boundary(arr: List[bool]) -> int:
    left_idx, right_idx = 0, len(arr)-1
    boundary_idx = -1
    
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx)//2
        
        if arr[mid_idx] is True:
            boundary_idx = mid_idx
            right_idx = mid_idx - 1
            
        else:
            left_idx = mid_idx + 1
            
    return boundary_idx
    

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
