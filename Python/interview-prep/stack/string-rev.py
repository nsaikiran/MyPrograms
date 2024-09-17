# Practice to include the type hints 
def string_rev(input_string: str):
    print("input string: ", input_string)
    stack = []
    # push all elements onto stack
    for c in input_string:
        stack.append(c)
    
    while stack:
        print(stack.pop(), end="")
    print("")

if __name__ == '__main__':
    # take input and reverse that
    string_rev(input())
    