"""
Asked in role specializatoin round of paypal
Maximize the sum of k numbers to be picked from an array of size n.

Rules
k  <= n
Numbers can be picked for summation only from the ends. This means that element 0 should be picked before element 1 and so on from left side. Similarly from right side, element n-1 should be picked before element n-2 and so on.
Although we can pick only end elements for summation, we are free to look at all the elements in the array.
Example, if there is an array like 3,5,1,1,1,1,8. The maximum sum when k = 3 is 16. (3 + 5 + 8)
"""
# https://www.geeksforgeeks.org/maximize-sum-of-k-elements-in-array-by-taking-only-corner-elements/


def recursive_approach(data, left_index_to_pick , right_index_to_pick, curr_sum, no_elements_to_pick):

    if not no_elements_to_pick:
        return curr_sum

    sum_when_picked_left = data[left_index_to_pick] + curr_sum
    sum_when_picked_right = data[right_index_to_pick] + curr_sum

    return max( recursive_approach(data, left_index_to_pick + 1, right_index_to_pick, sum_when_picked_left, no_elements_to_pick - 1 ), 
                recursive_approach(data, left_index_to_pick, right_index_to_pick - 1, sum_when_picked_right, no_elements_to_pick - 1) )

"""
THe above is recursive solution, it has overlapping subproblems and optimal substrucute (ptimal sol of subproblems make  up optimal solutoinm for the probl).

Exponenetial O(2^K)
At any point in time O(K) statck is used
"""


def recursive_approach_with_memo(data, left_index_to_pick , right_index_to_pick, curr_sum, no_elements_to_pick, memo):

    if not no_elements_to_pick:
        return curr_sum

    key = (left_index_to_pick , right_index_to_pick, no_elements_to_pick) #tuple
    if key in memo:
        print("found for ", key)
        return memo[key]

    sum_when_picked_left = data[left_index_to_pick] + curr_sum
    sum_when_picked_right = data[right_index_to_pick] + curr_sum

    result = max(   recursive_approach_with_memo(data, left_index_to_pick + 1, right_index_to_pick, sum_when_picked_left, no_elements_to_pick - 1, memo ), 
                    recursive_approach_with_memo(data, left_index_to_pick, right_index_to_pick - 1, sum_when_picked_right, no_elements_to_pick - 1, memo) )
    memo[(left_index_to_pick , right_index_to_pick, no_elements_to_pick)] = result

    return result


def two_pointer_optimzed(data, no_elements_to_pick):
    # Assume no of element to pick is less than half, otherwise they will overlap, any problem? or in this case can we optimize/
    if not no_elements_to_pick < len(data):
        return -1

    # pick all left elements.
    curr_max_sum = sum_seen_so_far = sum(data[:no_elements_to_pick])

    right_element_to_pick =  -1

    curr_left_index = no_elements_to_pick - 1

    while curr_left_index > 0:
        sum_seen_so_far = sum_seen_so_far - data[curr_left_index] + data[right_element_to_pick]
        curr_max_sum = max(sum_seen_so_far, curr_max_sum)
        curr_left_index -= 1
        right_element_to_pick -= 1
    return curr_max_sum





"""
THe above is recursive solution with memo,  reuse the existing subproblems
optimized better.
Exponenetial O(2^K)
At any point in time O(K) statck is used
"""



data_input = [8, 4, 4, 8, 12, 3, 2, 9]
K = 3

print("Recursibve")
print(recursive_approach(data_input, 0, len(data_input)-1, 0, K))

print("Recursibve with memo")
print(recursive_approach_with_memo(data_input, 0, len(data_input)-1, 0, K, dict()))

print("two poiner or liners")
print(two_pointer_optimzed(data_input, K))