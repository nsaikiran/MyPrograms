"""
The idea:
Bitwise OR is monotonic: meaning, either that will increase the result or keep it the same. 
In the arrays, we can compute the result till an index and see if we can add the next element to extend the subarray.
Because this is a sub-array, while expanding the result for the next element, we can only consider result ending at the present index (not the results ending at index before that)
"""

def count_valid_subarrays(arr):
    from collections import defaultdict

    result = 0
    prev = dict()  # OR value -> set of elements in contributing subarrays

    for num in arr:
        curr = defaultdict(set)

        # Start new subarray with only this element
        curr[num].add(num)

        # Extend previous subarrays
        for or_val, elements in prev.items():
            new_or = or_val | num
            curr[new_or].update(elements)
            curr[new_or].add(num)

        # Count valid subarrays
        for or_val, elements in curr.items():
            if or_val in elements:
                result += 1

        prev = curr

    return result
