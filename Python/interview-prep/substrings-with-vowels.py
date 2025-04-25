"""
Given a string composed of lowercase letters within the ASCII range 'a'-'z', determine the number of substrings that consist solely of vowels, where each vowel appears at least once. The vowels are ['a', 'e', 'i', 'o', 'u']. A substring is defined as a contiguous sequence of characters within the string.

Example

s = 'aeioaexaaeuiou'


There is a substring to the left that is made of vowels, 'aeioae' which is followed by an 'x'. Since 'x'is not a vowel, it cannot be included in the substring, and this substring does not contain all of the vowels. It is not a qualifying substring. Moving to the right, there are four substrings that do qualify: 'aaeuiou', 'aaeuio', 'aeuiou' and 'aeuio'.

"""
from collections import Counter

def count_ss_with_vowels(input_str):
    window = Counter()
    window_start_index = window_end_index = 0
    vowels = "aeiou" #['a', 'e', 'i', 'o', 'u']
    unique_qualified_strings = 0
    total_result = 0


    while window_end_index < len(input_str):
        current_char = input_str[window_end_index]

        if current_char in vowels:
            window[current_char] += 1

            if len(window.keys()) == 5: #all vowels present

                # see for duplicates at beginning
                # this loop will stop at a char with its count 1, which we can't remove.
                while window[input_str[window_start_index]] > 1:
                    window[input_str[window_start_index]] -= 1 #shrink
                    unique_qualified_strings += 1
                    window_start_index += 1

                #This while loop shouldn't alter the above if condition 
                
                total_result = total_result + 1 + unique_qualified_strings
                # unique_qualified_strings will be used for each character that keeps the condition, i.e duplicates on right side.
        else:
            # reset the substring seen sofar, as the char is not vowel
            window = Counter()
            unique_qualified_strings = 0
            window_start_index = window_end_index + 1

        window_end_index += 1
    return total_result


if __name__ == '__main__':
    print(count_ss_with_vowels("aeioaexaaeuiou"))