def linear_search(data, target):
    """
        Return the index position if the target element is found.
        If not, return None.
    """
    for ind in range(0, len(data)):
        if int(data[ind]) == target:
            return ind
    return None


def verify_index(ind):
    if ind is not None:
        print("Target found at index: ", ind)
    else:
        print("Target was not found in the list.")
    
if __name__ == "__main__":
    numbers_list = input("Enter a list of elements: ").split()
    search_elem = int(input("Enter the element to be searched: "))
    result = linear_search(numbers_list, search_elem)
    verify_index(result)