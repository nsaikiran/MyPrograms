"""
Given a list of numbers, for each element find its *next greater element* in anti-clock wise traversal. 
For ex: [4,15,0,7,3,6,11]
        [15,-1,7,11,6,11,15]
        
"""

"""
Brute force, O(N^2) solution. For each element we may visit all other elements once to find NGE.
"""
def nge_brute_force(input_array):
    no_of_elements = len(input_array)
    nge_array = [-1] * no_of_elements
    for index in range(no_of_elements):
        #print("outer",index)
        element = input_array[index]
        for next_index in range(index + 1, index + no_of_elements):
            #print(next_index)
            next_element = input_array[next_index % no_of_elements]
            if next_element > element:
                nge_array[index] = next_element
                break #found the NGE. Stop
    return nge_array


"""
Simplicification: NGE only on right side. We are looking for an immediate greater on the right side.
We traverse from the right side to maintain a stack to track the possible greater values on right side.
1. Current element can be a possible greater value for the elements on the left side. So push on to stack.
2. To find the immediate greater element, first remove all of the elements less or equal to the current element from stack.
3. Top of the stack will have the greater element, if nothing is there then it doesn't exist.
4. Push this current element onto stack.

O(N) complexity
"""
def nge_stack_right_side(input_array):
    number_of_elements = len(input_array)
    stack = []
    result = [-1] * number_of_elements

    for current_index in range(number_of_elements - 1, -1, -1):
        current_element = input_array[current_index]
        while stack and stack[-1] <= current_element:
            stack.pop()
        if stack:
            result[current_index] = stack[-1] #else is covered already at initialization
        stack.append(current_element)
    return result


"""
Now, we want to find the NGE for each element in the anti-clock wise direcation of circular iteration.
We will use stack. We assume that a copy of the input is attached to the input.
Here we are iterating from the end, but we can also iterate from 0 to 2n-1 index and do the same.
Because we are finding the NGE in circular fasion.
"""
def nge_stack_anti_clock_wise(input_array):
    number_of_elements = len(input_array)
    result = [-1] * number_of_elements
    stack = []

    for current_index in range(2 * number_of_elements - 1, -1 , -1):
        current_element = input_array[current_index % number_of_elements]
        # Remove all elements that are lesser or equal to current element
        while stack and stack[-1] <= current_element:
            stack.pop()
        
        # Update the result only if we are in the range of array. 
        # The important thing is the stack is populated with possible greater elements by the time we reach index < len of array.
        if current_index < number_of_elements:
            if stack:
                result[current_index] = stack[-1]
        stack.append(current_element)

    return result

if __name__ == "__main__":
    input_array = [4,15,0,7,3,6,11]
    print("input array: ", input_array)
    print("Brute force: ", nge_brute_force(input_array))
    input_array = [4,15,0,7,3,6,11]
    print("Stack solution: ", nge_stack_anti_clock_wise(input_array))

    print("----")
    print("NGE only on right side:", nge_stack_right_side(input_array))
    print("")