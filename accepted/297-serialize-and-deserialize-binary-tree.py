# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class Codec:
    def serialize(self, root):
        stack = [root, ]
        result = ''
        
        while len(stack) > 0:
            top = stack.pop()
            if top is not None:
                stack.append(top.right)
                stack.append(top.left)
                result += (str(top.val) + ' ')
            else:
                result += '. '
        
        return result.strip()

    def deserialize(self, data):
        if len(data) == 0 or data == '.':
            return None
        
        tree = data.split(' ')
        root = TreeNode(tree[0])
        stack = []
        cur = root
        
        for i in xrange(1, len(tree)):
            node = None if tree[i] == '.' else TreeNode(int(tree[i]))
            if cur is not None:
                cur.left = node
                stack.append(cur)
                cur = cur.left
            else:
                stack.pop().right = node
                cur = node
        
        return root
