from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root: TreeNode) :
    columnTable = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()

        if node is not None:
            columnTable[column].append(node.val)

            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))

    return [columnTable[x] for x in sorted(columnTable.keys())]


print(verticalOrder(root))



