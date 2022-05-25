def recursive_binary_search(data, target):
    if len(data) == 0:
        return False
    else:
        mid_point = (len(data)) // 2
        print("----------")
        print(data[mid_point])
        if (data[mid_point]) == target:
            return True
        else:
            if data[mid_point] < target:
                print(sorted(data[mid_point+1:]))
                return recursive_binary_search(data[mid_point+1:], target)
            else:
                print(sorted(data[:mid_point-1]))
                return recursive_binary_search(data[:mid_point], target)

def verify_index(result):
    print("Target found? ", result)


if __name__ == "__main__":
    numbers_list = input("Enter a sorted list of elements: ").split()
    search_elem = int(input("Enter the element to be searched: "))
    result = recursive_binary_search(sorted(list(map(int, numbers_list))), search_elem)
    verify_index(result)
