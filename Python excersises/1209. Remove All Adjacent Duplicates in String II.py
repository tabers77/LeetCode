class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
            stack = []
            counter_stack = []
            for letter in s:
                if not stack or stack[-1] != letter:
                    stack.append(letter)
                    counter_stack.append(1)
                elif stack[-1] == letter:
                    counter_stack[-1] += 1
                if counter_stack[-1] == k:
                    counter_stack.pop()
                    stack.pop()
            return ''.join([stack[i] * counter_stack[i] for i in range(len(stack))])
