from collections import deque

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

class Algorithms:
    @staticmethod
    def pre_order(node):
        if node:
            print(node.val)
            Algorithms.pre_order(node.left)
            Algorithms.pre_order(node.right)

    @staticmethod
    def pre_order_iterative(node):
        if node is None:
            return []
        todo_stack = Stack()
        todo_stack.push(node)
        while not todo_stack.empty():
            cur_node = todo_stack.pop()
            print(cur_node.val)
            if cur_node.right:
                todo_stack.push(cur_node.right)
            if cur_node.left:
                todo_stack.push(cur_node.left)

    @staticmethod
    def in_order(node):
        if node:
            Algorithms.in_order(node.left)
            print(node.val)
            Algorithms.in_order(node.right)

    @staticmethod
    def in_order_iterative(node):
        if node is None:
            return []
        todo_stack = []
        cur_node = node
        while todo_stack or cur_node:
            while cur_node:
                todo_stack.append(cur_node)
                cur_node = cur_node.left
            
            cur_node = todo_stack.pop()
            print(cur_node.val)
            cur_node = cur_node.right

    @staticmethod
    def post_order(node):
        if node:
            Algorithms.post_order(node.left)
            Algorithms.post_order(node.right)
            print(node.val)

    @staticmethod
    def post_order_iterative(node):
        if node is None:
            return []
        todo_stack = [node]
        result_stack = []
        while todo_stack:
            cur_node = todo_stack.pop()
            if cur_node.left:
                todo_stack.append(cur_node.left)
            if cur_node.right:
                todo_stack.append(cur_node.right)
            result_stack.append(cur_node)
        while result_stack:
            cur_node = result_stack.pop()
            print(cur_node.val)

    @staticmethod
    def layer_order(node):
        todo_queue = deque()
        todo_queue.append(node)
        while todo_queue:
            cur_node = todo_queue.popleft()
            if cur_node.left:
                todo_queue.append(cur_node.left)
            if cur_node.right:
                todo_queue.append(cur_node.right)
            print(cur_node.val)

    @staticmethod
    def build_tree_by_pre_in(pre_order, in_order):
        assert len(pre_order) == len(in_order)
        if not pre_order:
            return None
        root_val = pre_order[0]
        idx = in_order.index(root_val)  # could throw exception
        left_length = idx
        node = Node(root_val)
        node.left = Algorithms.build_tree_by_pre_in(pre_order[1:(left_length+1)], in_order[:left_length])
        node.right = Algorithms.build_tree_by_pre_in(pre_order[(left_length+1):], in_order[(idx+1):])
        return node

    @staticmethod
    def build_tree_by_pre_in_iterative(pre_order, in_order):
        assert len(pre_order) == len(in_order)
        if not pre_order:
            return None
        root_val = pre_order[0]
        node = Node(root_val)
        if len(pre_order) <= 1:
            node.left = node.right = None
            return node

        root_stack = [node]
        in_order_idx = 0
        for value in pre_order[1:]:
            cur_root = root_stack[-1]
            cur_node = Node(value)
            if cur_root == in_order[in_order_idx]:  # no left tree
                while root_stack and root_stack[-1].val == in_order[in_order_idx]:
                    root_stack.pop()
                    in_order_idx += 1
                cur_root.right = cur_node
            else:
                cur_root.left = cur_node
            root_stack.append(cur_node)
        return node

    @staticmethod
    def build_tree_by_pre_post(pre_order, post_order):
        assert len(pre_order) == len(post_order)
        if not pre_order:
            return [None]
        assert pre_order[0] == post_order[-1], "{}, {}".format(pre_order, post_order)
        root_val = pre_order[0]
        if len(pre_order) > 1:
            left_root = pre_order[1]
            idx = post_order.index(left_root)
            left_lengths = [idx + 1]
            if idx == len(post_order) - 2:
                left_lengths.append(0)
        else:
            left_lengths = [0]
        
        results = []
        for left_length in left_lengths:
            node = Node(root_val)
            for left in Algorithms.build_tree_by_pre_post(pre_order[1:(left_length+1)], post_order[:left_length]):
                for right in Algorithms.build_tree_by_pre_post(pre_order[(left_length+1):], post_order[left_length:-1]):
                    node.left = left
                    node.right = right
                    results.append(node)
        return results

    @staticmethod
    def build_tree_by_post_in(post_order, in_order):
        assert len(post_order) == len(in_order)
        if not post_order:
            return None
        root_val = post_order[-1]
        idx = in_order.index(root_val)
        left_length = idx
        node = Node(root_val)
        node.left = Algorithms.build_tree_by_post_in(post_order[:left_length], in_order[:left_length])
        node.right = Algorithms.build_tree_by_post_in(post_order[left_length:-1], in_order[(left_length+1):])
        return node

    @staticmethod
    def get_post_by_pre_in(pre_order, in_order):
        assert len(pre_order) == len(in_order)
        if not pre_order:
            return []

        root_val = pre_order[0]
        idx = in_order.index(root_val)
        left_length = idx
        result_list = []
        result_list.extend(Algorithms.get_post_by_pre_in(pre_order[1:(left_length+1)], in_order[:left_length]))
        result_list.extend(Algorithms.get_post_by_pre_in(pre_order[(left_length+1):], in_order[(left_length+1):]))
        result_list.append(root_val)
        return result_list

    @staticmethod
    def get_post_by_pre_in_iterative(pre_order, in_order):
        assert len(pre_order) == len(in_order)
        if not pre_order:
            return None
        todo_stack = [[0, 0, len(pre_order)]]
        result_stack = []
        while todo_stack:
            pre_start, in_start, length = todo_stack.pop()
            root_val = pre_order[pre_start]
            idx = in_order.index(root_val)
            left_length = idx - in_start
            assert left_length >= 0
            right_length = length - left_length - 1
            assert right_length >= 0
            if left_length > 0:
                todo_stack.append([pre_start + 1, in_start, left_length])
            if right_length > 0:
                todo_stack.append([pre_start + left_length + 1, in_start + left_length + 1, right_length])
            
            cur_node = Node(root_val)
            result_stack.append(cur_node)
        while result_stack:
            print(result_stack.pop().val)

    @staticmethod
    def inverse_tree(node):
        if node:
            node.left, node.right = node.right, node.left
            Algorithms.inverse_tree(node.left)
            Algorithms.inverse_tree(node.right)
        return node

    @staticmethod
    def inverse_tree_iterative(node):
        if node is None:
            return node
        todo_stack = Stack()
        todo_stack.push(node)
        while not todo_stack.empty():
            cur_node = todo_stack.pop()
            if cur_node.left:
                todo_stack.push(cur_node.left)
            if cur_node.right:
                todo_stack.push(cur_node.right)
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
        return node

    @staticmethod
    def inverse_tree_queue(node):
        import queue
        if node is None:
            return node
        todo_queue = queue.Queue()
        todo_queue.put(node)
        while todo_queue.qsize() > 0:
            cur_node = todo_queue.get()
            if cur_node.left:
                todo_queue.put(cur_node.left)
            if cur_node.right:
                todo_queue.put(cur_node.right)
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
        return node

    @staticmethod
    def is_sym(node):
        def is_sym_two(node_1, node_2):
            if node_1 is None and node_2 is None:
                return True
            if node_1 and node_2:
                if node_1.val != node_2.val:
                    return False
                if is_sym_two(node_1.left, node_2.right):
                    if is_sym_two(node_1.right, node_2.left):
                        return True
                return False
            return False

        if not node:
            return True
        return is_sym_two(node.left, node.right)

    @staticmethod
    def is_sym_iterative(node):
        if not node:
            return True
        todo_stack = [[node.left, node.right]]
        while todo_stack:
            node_1, node_2 = todo_stack.pop()
            if node_1 is None and node_2 is None:
                continue
            if node_1 and node_2:
                if node_1.val == node_2.val:
                    todo_stack.append([node_1.left, node_2.right])
                    todo_stack.append([node_1.right, node_2.left])
                else:
                    return False
            else:
                return False
        return True
    
def main():
    import sys
    print(sys.version)
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))
    pre_order = [1, 2, 4, 5, 3, 6]
    in_order = [4, 2, 5, 1, 3, 6]
    post_order = [4, 5, 2, 6, 3, 1]
    sym_tree = Node(1, Node(2, Node(4), Node(5)), Node(2, Node(5), Node(4)))
    build_tree = Algorithms.build_tree_by_pre_in_iterative(pre_order, in_order)
    Algorithms.pre_order(build_tree)

main()
