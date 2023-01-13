from typing import List

# SOLUTION USING ONLY A LIST

container = list()


def depthSum(nestedList, depth=0):
    def dfs(lst, depth):
        depth += 1
        depthSum(lst, depth)

    for item in nestedList:
        if isinstance(item, list):
            dfs(item, depth)
        else:
            depth2 = depth + 1
            container.append((item, depth2))
    res = 0
    for i in container:
        res += i[0] * i[1]
    return res


lst = [1, [4, [6]]]
print(depthSum(nestedList=lst))


# DFS SOLUTION
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):
            total = 0
            for nested in nested_list:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += dfs(nested.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)
