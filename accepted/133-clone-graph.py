# https://leetcode.com/problems/clone-graph/
# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return None
        
        queue = [node, ]
        map = {node.label: UndirectedGraphNode(node.label), }
        
        while len(queue) > 0:
            next = queue.pop(0)
            cur = map[next.label]
            
            for sub in next.neighbors:
                if sub.label in map:
                    cur.neighbors.append(map[sub.label])
                else:
                    new = UndirectedGraphNode(sub.label)
                    map[sub.label] = new
                    cur.neighbors.append(new)
                    queue.append(sub)
        
        return map[node.label]
