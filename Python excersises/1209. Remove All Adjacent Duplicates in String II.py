
def removeDuplicates(s: str, k: int) -> str:
    stack = []
    counter_stack = []
    for letter in s:
        # if no list or last letter in stack != to current letter append that letter to stack and count 1
        if not stack or stack[-1] != letter:
            stack.append(letter)
            counter_stack.append(1)

        # if last letter in stack == letter , count 1 for that letter to count the duplicates
        elif stack[-1] == letter:
            counter_stack[-1] += 1

        if counter_stack[-1] == k:
            # I I reach the limit , ex [1,3] and k = 3 I remove last character
            counter_stack.pop()
            stack.pop()

    # Return final answer by multiplying the stack times the counter stack
    return ''.join([stack[i] * counter_stack[i] for i in range(len(stack))])


s = "deeedbbcccbdaa"
k = 3

print(removeDuplicates(s, k))
