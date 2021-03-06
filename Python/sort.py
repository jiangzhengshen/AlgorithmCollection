import copy

class Algorithms:
    @staticmethod
    def insertion_sort(data_list):
        if len(data_list) <= 1:
            return
        for idx in range(len(data_list)):
            cur_value = data_list[idx]
            for sort_idx in range(idx):
                if cur_value <= data_list[sort_idx]:
                    # insert to sort_idx
                    for insert_idx in range(idx - 1, sort_idx - 1, -1):
                        data_list[insert_idx + 1] = data_list[insert_idx]
                    data_list[sort_idx] = cur_value
                    break

    @staticmethod
    def quick_sort(data_list, left=0, right=None):
        def partition(data, left, right):
            pivot = data[left]
            first_larger_idx = left + 1
            for idx in range(left + 1, right):
                if data[idx] < pivot:
                    data[idx], data[first_larger_idx] = data[first_larger_idx], data[idx]
                    first_larger_idx += 1
            data[left], data[first_larger_idx-1] = data[first_larger_idx-1], data[left]
            return first_larger_idx - 1

        if not data_list:
            return
        if right is None:
            right = len(data_list)
        if right - left <= 1:
            return data_list
        mid = partition(data_list, left, right)
        Algorithms.quick_sort(data_list, left, mid)
        Algorithms.quick_sort(data_list, mid+1, right)

    @staticmethod
    def quick_sort_iterative(data_list):
        def partition(left, right):
            pivot = data_list[left]
            first_larger_idx = left + 1
            for idx in range(left+1, right):
                if data_list[idx] < pivot:
                    data_list[idx], data_list[first_larger_idx] = data_list[first_larger_idx], data_list[idx]
                    first_larger_idx += 1
            data_list[left], data_list[first_larger_idx - 1] = data_list[first_larger_idx - 1], data_list[left]
            return first_larger_idx - 1
        todo_stack = [[0, len(data_list)]]
        while todo_stack:
            left, right = todo_stack.pop()
            if right - left <= 1:
                continue
            mid = partition(left, right)
            todo_stack.append([left, mid])
            todo_stack.append([mid+1, right])

    @staticmethod
    def heap_sort_heapq(data_list):
        import heapq
        ret_list = []
        heapq.heapify(data_list)
        for i in range(len(data_list)):
            ret_list.append(heapq.heappop(data_list))
        return ret_list

    @staticmethod
    def heap_sort_manual(data_list):
        def heapify(data, root_idx, capacity):
            # suppose subtree are all heaps
            left = 2 * root_idx + 1
            right = 2 * root_idx + 2
            smallest = root_idx
            if left < capacity and data[left] < data[smallest]:
                smallest = left
            if right < capacity and data[right] < data[smallest]:
                smallest = right
            if smallest != root_idx:
                data[smallest], data[root_idx] = data[root_idx], data[smallest]
                heapify(data, smallest, capacity)

        length = len(data_list)
        if length <= 1:
            return data_list
        
        for idx in reversed(range(length // 2)):
            heapify(data_list, idx, length)

        ret_list = []
        for last_idx in reversed(range(length)):
            ret_list.append(data_list[0])
            data_list[0] = data_list[last_idx]
            heapify(data_list, 0, last_idx)
        return ret_list

    @staticmethod
    def merge_sort(data_list, left=0, right=None):
        def merge(left, mid, right):
            if mid == 0 or mid == len(data_list) or data_list[mid - 1] <= data_list[mid]:
                return
            if mid - left == 0 or right - mid == 0:
                return
            a_list = data_list[left:mid]
            b_list = data_list[mid:right]
            a_head = 0
            b_head = 0

            first_unorder_idx = left
            while first_unorder_idx < right:
                if b_head >= len(b_list) or (a_head < len(a_list) and a_list[a_head] <= b_list[b_head]):
                    data_list[first_unorder_idx] = a_list[a_head]
                    a_head += 1
                else:
                    data_list[first_unorder_idx] = b_list[b_head]
                    b_head += 1
                first_unorder_idx += 1

        if right is None:
            right = len(data_list)
        if right - left <= 1:
            return
        mid = (left + right) // 2
        Algorithms.merge_sort(data_list, left, mid)
        Algorithms.merge_sort(data_list, mid, right)
        merge(left, mid, right)

    @staticmethod
    def merge_sort_inplace(data_list):
        pass

    @staticmethod
    def merge_sort_iterative(data_list):
        def merge(left, mid, right):
            if mid - left == 0 or right - mid == 0 or data_list[mid - 1] <= data_list[mid]:
                return
            a_list = data_list[left:mid]
            b_list = data_list[mid:right]
            a_head = 0
            b_head = 0

            for idx in range(left, right):
                if b_head >= len(b_list) or (a_head < len(a_list) and a_list[a_head] <= b_list[b_head]):
                    data_list[idx] = a_list[a_head]
                    a_head += 1
                else:
                    data_list[idx] = b_list[b_head]
                    b_head += 1

        if len(data_list) <= 1:
            return
        cur_left_right = [0, len(data_list)]
        todo_stack = [cur_left_right]
        merge_stack = []
        while todo_stack:
            left, right = todo_stack.pop()
            mid = (left + right) // 2
            if mid - left > 1:
                todo_stack.append([left, mid])
            if right - mid > 1:
                todo_stack.append([mid, right])

            merge_stack.append([left, right])
        while merge_stack:
            left, right = merge_stack.pop()
            mid = (left + right) // 2
            merge(left, mid, right)

    @staticmethod
    def bubble_sort(data_list):
        for i in range(len(data_list)):
            for j in range(i + 1, len(data_list)):
                if data_list[i] > data_list[j]:
                    data_list[i], data_list[j] = data_list[j], data_list[i]


def main():
    import random
    test_list = [random.randint(1, 20) for i in range(10)]
    print(test_list)
    test_list = Algorithms.heap_sort_manual(test_list)
    print(test_list)

main()
