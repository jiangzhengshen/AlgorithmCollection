
def grid_count(rows, columns):
    assert rows > 0 and columns > 0
    if rows == 1 or columns == 1:
        return 1
    return grid_count(rows - 1, columns) + grid_count(rows, columns - 1)

def max_sum(data_list):
    def max_sum_end_idx(data_list, end_idx):
        assert end_idx >= 0
        if end_idx == 0:
            return data_list[end_idx]
        sub_max = max_sum_end_idx(data_list, end_idx - 1)
        if sub_max <= 0:
            return data_list[end_idx]
        else:
            return sub_max + data_list[end_idx]

    if len(data_list) == 0:
        return 0
    
    max_result = data_list[0]
    for last_idx in range(1, len(data_list)):
        cur_max = max_sum_end_idx(data_list, last_idx)
        if max_result < cur_max:
            max_result = cur_max
    return max_result

def max_sum_iterative(data_list):
    if len(data_list) == 0:
        return None

    max_result = data_list[0]
    last_max_result_end_idx = data_list[0]
    for last_idx in range(1, len(data_list)):
        if last_max_result_end_idx <= 0:
            cur_max_result = data_list[last_idx]
        else:
            cur_max_result = last_max_result_end_idx + data_list[last_idx]
        if cur_max_result > max_result:
            max_result = cur_max_result
        last_max_result_end_idx = cur_max_result
    return max_result

def longest_increase_substring(data_list):
    if len(data_list) == 0:
        return None
    
    max_result = 1
    last_max_end_idx = 1
    for end_idx in range(1, len(data_list)):
        if data_list[end_idx] >= data_list[end_idx - 1]:
            last_max_end_idx += 1
        else:
            last_max_end_idx = 1
        if last_max_end_idx > max_result:
            max_result = last_max_end_idx
    return max_result

def matrix_multiply(matrix_size_list):
    pass

def longest_common_substring(a_list, b_list):
    pass

import random
# print(grid_count(3, 7))
test_list = [random.randint(-10, 10) for _ in range(10)]
print(test_list)
print(longest_increase_substring(test_list))
