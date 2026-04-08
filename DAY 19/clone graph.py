class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        cloned = {}    # original → clone mapping

        from collections import deque
        queue = deque([node])
        cloned[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                cloned[curr].neighbors.append(
                    cloned[neighbor]
                )

        return cloned[node]