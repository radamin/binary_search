"""(Procedural programming - is based on a function) +
+ (the function itself gives instructions on how to do)"""
def binary_search(numbers, value, min_index, max_index):
    """The function returns -1 when the searched element is not in the array"""
    if max_index < min_index:
        return -1

    mid = (max_index - min_index) // 2 + min_index

    if numbers[mid] < value:
        return binary_search(numbers, value, mid + 1, max_index)

    if numbers[mid] > value:
        return binary_search(numbers, value, min_index, mid - 1)

    return mid


my_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 19, 91, 101]
num = int(input("Enter number: "))
print(binary_search(my_nums, num, 0, len(my_nums) - 1))
