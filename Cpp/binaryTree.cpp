#include <vector>
#include <iostream>

int binarySearch(std::vector<int> list, int target) {
    int begin = 0, end = list.size();
    while(begin < end) {
        int mid = (begin + end) / 2;
        if(list[mid] > target) {
            end = mid;
        } else if(list[mid] < target) {
            begin = mid + 1;
        } else {
            return mid;
        }
    }
    return -1;
}

int main() {
    int array[5] = {3, 6, 9, 11, 20};
    std::vector<int> testList(array, array + 5);
    std::cout << binarySearch(testList, 6);
}
