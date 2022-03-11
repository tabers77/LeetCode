class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        characters = [i for i in s]
        open_par_stack = []
        for idx, i in enumerate(characters):
            if i == '(':
                open_par_stack.append(idx)
            elif i == ')':
                if open_par_stack:
                    open_par_stack.pop()
                else:
                    characters[idx] = ''

        while open_par_stack:
            open_par_idx = open_par_stack.pop()
            characters[open_par_idx] = ''

        return ''.join(characters)
