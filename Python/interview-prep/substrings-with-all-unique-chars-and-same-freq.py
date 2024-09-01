
"""
Given a string with few unique characters repeating.
Print substrings containing unique characters and having same frequency
"""
from collections import defaultdict

"""
Solution:
X - no. of unique characters
Generate all substrings of the string, and check if substring has all unique characters and they have same count

1. First loop O(N)
2. Second loop O(N)
3. Third loop O(N) - it goes over the substring and finds frequency of each char
4. Check of len(set(freq.values())) will be O(X)

Overall time: O(N*N*N*X)
Overall space: O(X)
"""
def brute_force(input_str):
    print("input string:", input_str)
    print("substrings:")
    unique_chars = set(input_str)
    unique_chars_count = len(unique_chars)

    for i in range(0, len(input_str)):
        for j in range(i, len(input_str)):
            # i = start index
            #j = end index
            freq = defaultdict(int)
            for k in range(i, j+1):
                freq[input_str[k]] += 1
            #print(freq)
            if len(freq) == unique_chars_count and len(set(freq.values())) == 1:
                print(input_str[i:j+1])

# -----------

"""
Optimization over above solution
Here, we are removing the 3rd for loop using sliding window.

1. First loop O(N)
2. Second loop O(N)
3. Check of len(set(freq.values())) will be O(X)

Overall time: O(N*N*X)
Overall space: O(X)
"""
# optimization 1
# use sliding window to remove the inner for loop
def sliding_window(input_str):
    print("input string:", input_str)
    print("substrings:")
    unique_chars = set(input_str)
    unique_chars_count = len(unique_chars)

    for i in range(0, len(input_str)):
        freq = defaultdict(int)
        for j in range(i, len(input_str)):
            freq[input_str[j]] += 1
            if len(freq) == unique_chars_count and len(set(freq.values())) == 1:
                print(input_str[i:j+1])

# ------------


"""
Further optimization over the above:
We know the unique characters count, so we can infer the substrings have all unique characters with same count.
Hence, the valid substrings will have length multiples of unique character count.

X - unique char count

Complexity analysis:
1. First loop will go over logX (N)
2. Inner code takes O(N) as we go over all characters once. (Though we've two while loops it takes O(N))
3. Check of len(set(freq.values())) will be O(X)

So time complexity is O(N * X * logX N)
Space complexity is: O(X)
"""

# check for only valid length substrings
def sliding_window_and_specific_length_substrings(input_str):
    print("input string:", input_str)
    print("substrings:")
    unique_chars = set(input_str)
    unique_chars_count = len(unique_chars)

    for substring_length in range(unique_chars_count, len(input_str)+1, unique_chars_count):
        # generate the window
        window_start, next_char_index = 0, 0
        freq = defaultdict(int)
        while next_char_index < substring_length:
            freq[input_str[next_char_index]] += 1
            next_char_index += 1
        # verify the window
        if len(freq) == unique_chars_count and len(set(freq.values())) == 1:
                print(input_str[window_start:next_char_index])
        
        # see if there is possibility from next window
        while next_char_index < len(input_str):
            freq[input_str[window_start]] -= 1
            if not freq[input_str[window_start]]:
                del freq[input_str[window_start]]
            freq[input_str[next_char_index]] += 1
            next_char_index += 1
            window_start += 1
            # verify the window
            if len(freq) == unique_chars_count and len(set(freq.values())) == 1:
                print(input_str[window_start:next_char_index])

# ------------- 

"""
Here, the check of count tracking is optimized. 
Previously, we were using len(set(freq.values())), which takes O(X) where X is the unique character count.
Now it'll be O(1)

X - unique char count

Complexity analysis:
1. First loop will go over logX (N)
2. Inner code takes O(N) as we go over all characters once. (Though we've two while loops it takes O(N))

So time complexity is O(N logX N), which is better than O(N*N)
Space complexity is: O(X) + O(X)
"""

# check for only valid length substrings
def optimze_same_count_verification(input_str):
    print("input string:", input_str)
    print("substrings:")
    unique_chars = set(input_str)
    unique_chars_count = len(unique_chars)

    # For each possible substring_length
    for substring_length in range(unique_chars_count, len(input_str)+1, unique_chars_count):
        window_start, next_char_index = 0, 0
        freq = defaultdict(int)
        freq_count = defaultdict(int)
        
        # generate the initial window
        while next_char_index < substring_length:
            next_char = input_str[next_char_index]
            freq[next_char] += 1
            next_char_index += 1
        
        # Generate the freq_count map
        ## Assuming the dictionary in any language provides an iterator
        for key, value in freq.items():
            freq_count[value] += 1

        # verify the initial window
        if len(freq) == unique_chars_count and len(freq_count) == 1:
                print(input_str[window_start:next_char_index])
        
        # From now, slide the window, as long as the next_char_index is valid
        while next_char_index < len(input_str):
            next_char = input_str[next_char_index]

            # Remove the first character of the window
            # 1. Update freq_count as the first character will have its count updated soon in freq
            freq_count[freq[input_str[window_start]]] -= 1
            if not freq_count[freq[input_str[window_start]]]:
                del freq_count[freq[input_str[window_start]]]
            
            # 2. Update the count of first character in freq (deletion of first character from window)
            freq[input_str[window_start]] -= 1
            if not freq[input_str[window_start]]:
                del freq[input_str[window_start]]
            else:
                freq_count[freq[input_str[window_start]]] += 1
            
            # Add next_char to window
            # 1. If next_char alerady exists in the freq map then reduce that
            if next_char in freq:
                freq_count[freq[next_char]] -= 1
                if not freq_count[freq[next_char]]:
                    del freq_count[freq[next_char]]
            # 2. Add element
            freq[next_char] += 1
            # 3. Add elements count to freq_count map
            freq_count[freq[next_char]] += 1

            # Increment nex_char-index and window_start_index
            next_char_index += 1
            window_start += 1

            # Verify window [window_start_index: next_char_index)
            if len(freq) == unique_chars_count and len(freq_count) == 1:
                print(input_str[window_start:next_char_index])
  
"""
Note: Deleting the character once its count reaches 0 is important. Maybe we can create a subclass of defaultdict(int) which deletes the item once it count reaches 0.
"""

if __name__ == "__main__":

    print("brute_force")
    brute_force("RBRRB")
    print("sliding_window")
    sliding_window("RBRRB")
    print("sliding_window_and_specific_length_substrings")
    sliding_window_and_specific_length_substrings("RBRRB")
    print("optimze_same_count_verification")
    optimze_same_count_verification("RBRRB")
    # Set 2
    print("Input set 2")
    optimze_same_count_verification("aabbcc")
