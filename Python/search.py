
class Algorithms:
    @staticmethod
    def binary_search(data_list, element):
        begin_idx = 0
        end_idx = len(data_list)
        while begin_idx < end_idx:
            mid = (begin_idx + end_idx) // 2
            if data_list[mid] > element:
                end_idx = mid
            elif data_list[mid] < element:
                begin_idx = mid + 1
            else:
                return mid, True
        assert begin_idx == end_idx
        return begin_idx, False

    @staticmethod
    def shuffle(data_list):
        import random
        total = len(data_list)
        for i in range(total):
            random_idx = random.randint(i, total - 1)
            if i != random_idx:
                data_list[i], data_list[random_idx] = data_list[random_idx], data_list[i]
        return data_list

    @staticmethod
    def breadth_first_search():
        pass

    @staticmethod
    def depth_first_search():
        pass

    @staticmethod
    def eight_queens(queen_columns, cur_row=0):
        total_count = 0
        if cur_row == len(queen_columns):
            return 1
        
        total_columns = len(queen_columns)
        for column in range(total_columns):
            is_valid = True
            for row in range(cur_row):
                if queen_columns[row] == column or cur_row - row == abs(column - queen_columns[row]):
                    is_valid = False
                    break
            if is_valid:
                queen_columns[cur_row] = column
                total_count += Algorithms.eight_queens(queen_columns, cur_row + 1)
        return total_count

def test_binary_search():
    test_list = list(range(100))
    result_idx, is_found = Algorithms.binary_search(test_list, 15)
    if is_found:
        print(is_found, result_idx, test_list[result_idx])
    else:
        print(is_found, result_idx)

def test_shuffle():
    # test_list = list(range(100))
    # result_list = Algorithms.shuffle(test_list)
    # print(result_list)
    print(Algorithms.eight_queens([None] * 8))

test_shuffle()
