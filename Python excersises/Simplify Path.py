# def simplifyPath(path: str) -> str:
#     s = ''
#     if path[0] == '/':
#
#         for i in range(len(path)):
#
#             if path[i].isalpha():
#                 s += path[i]
#
#             if i + 1 == len(path) and path[i] == '/':
#                 s += ''
#
#             elif path[i] == '/':
#                 if s != '':
#                     if s[-1] != '/':
#                         s += '/'
#                     else:
#                         s += ''
#                 else:
#                     s += '/'
#
#             elif i != 0 and i + 1 != len(path) and path[i] == '/':
#                 s += path[i]
#     return s


# def simplifyPath(path: str) -> str:
#     stacked = list()
#
#     split_ = path.split('/')
#     if split_[-1] == '':
#         split_.pop()
#
#     if split_[0] == '':
#         for i in range(len(split_)):
#             if split_[i] == '' or split_[i] == '.':
#                 if split_[i] == '':
#                     if stacked:
#                         if stacked[-1] == '/':
#                             continue
#                         else:
#                             stacked.append('/')
#
#             elif split_[i].isalpha():
#                 stacked.append(split_[i])
#             # elif split_[i] == '.':
#             #     pass
#             elif split_[i] == '..' and stacked:
#                 if i - 1 != 0:
#                     stacked.pop()
#                 else:
#                     continue
#
#     stacked = '/' + ''.join(stacked)
#     return stacked
#
# path = "/a/../../b/../c//.//"
# #path =  "/home//foo/"
# print(simplifyPath(path))


# # CORRECT ANSWER
def simplifyPath(path: str) -> str:
    # Initialize a stack
    stack = []

    # Split the input string on "/" as the delimiter
    # and process each portion one by one
    for portion in path.split("/"):

        # If the current component is a "..", then
        # we pop an entry from the stack if it's non-empty
        if portion == "..":
            if stack:
                stack.pop()
        elif portion == "." or not portion:
            # A no-op for a "." or an empty string
            continue
        else:
            # Finally, a legitimate directory name, so we add it
            # to our stack
            stack.append(portion)

    # Stich together all the directory names together
    final_str = "/" + "/".join(stack)
    return final_str


path = "/a/../../b/../c//.//"
# expcted "/c"
print(simplifyPath(path))
