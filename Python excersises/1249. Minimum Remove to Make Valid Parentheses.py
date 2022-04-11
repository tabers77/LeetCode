# for every ( bracket I remove one )


def minRemoveToMakeValid(s: str):
    characters = [i for i in s]
    open_par_stack = []

    # Give an index to every character
    for idx, i in enumerate(characters):
        # Append to open_par_stack if I find an open bracket
        if i == '(':
            open_par_stack.append(idx)
        elif i == ')':
            # if there is a close bracket and if open_par_stack is not empty remove the last character
            if open_par_stack:
                open_par_stack.pop()
            else:
                # if there is a close bracket and if there are no brackets in open_par_stack
                # replace the character with an empty string
                characters[idx] = ''

    while open_par_stack:
        open_par_idx = open_par_stack.pop()
        # this part generates the final answer
        characters[open_par_idx] = ''

    # Remove extra bracket
    return ''.join(characters)


s = "lee(t(c)o)de)"
print(minRemoveToMakeValid(s))