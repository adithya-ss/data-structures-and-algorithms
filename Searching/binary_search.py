def binary_search(data, target):
    first_elem = 0
    last_elem = len(data) - 1

    while first_elem <= last_elem:
        mid_elem = (first_elem + last_elem) // 2
        if int(data[mid_elem]) == target:
            return mid_elem
        elif int(data[mid_elem]) < target:
            first_elem = mid_elem + 1
        else:
            last_elem = mid_elem - 1
        
    return None

def verify_index(ind):
    if ind is not None:
        print("Target found at index: ", ind)
    else:
        print("Target was not found in the list.")

if __name__ == "__main__":
    numbers_list = input("Enter a sorted list of elements: ").split()
    search_elem = int(input("Enter the element to be searched: "))
    result = binary_search(sorted(numbers_list), search_elem)
    verify_index(result)
