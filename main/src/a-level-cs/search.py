# Liner search algorithm

def linear_search(arr, target):
    """
    Perform a linear search for the target in the array.

    :param arr: List of elements to search through.
    :param target: The element to search for.
    :return: The index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def linear_search_all(arr, target):
    """
    Perform a linear search for all occurrences of the target in the array.

    :param arr: List of elements to search through.
    :param target: The element to search for.
    :return: A list of indices where the target is found.
    """
    indices = []
    for index, value in enumerate(arr):
        if value == target:
            indices.append(index)
    return indices if indices else -1


def linear_search_first(arr, target):
    """
    Perform a linear search for the first occurrence of the target in the array.

    :param arr: List of elements to search through.
    :param target: The element to search for.
    :return: The index of the first occurrence of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def linear_search_last(arr, target):
    """
    Perform a linear search for the last occurrence of the target in the array.

    :param arr: List of elements to search through.
    :param target: The element to search for.
    :return: The index of the last occurrence of the target if found, otherwise -1.
    """
    for index in range(len(arr) - 1, -1, -1):
        if arr[index] == target:
            return index
    return -1


def linear_search_count(arr, target):
    """
    Count the number of occurrences of the target in the array.

    :param arr: List of elements to search through.
    :param target: The element to count.
    :return: The count of occurrences of the target.
    """
    count = 0
    for value in arr:
        if value == target:
            count += 1
    return count


def linear_search_exists(arr, target):
    """
    Check if the target exists in the array.

    :param arr: List of elements to search through.
    :param target: The element to check for existence.
    :return: True if the target exists, otherwise False.
    """
    for value in arr:
        if value == target:
            return True
    return False


def linear_search_index(arr, target):
    """
    Get the index of the first occurrence of the target in the array.

    :param arr: List of elements to search through.
    :param target: The element to find the index of.
    :return: The index of the first occurrence of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def linear_search_all_indices(arr, target):
    """
    Get all indices of the target in the array.

    :param arr: List of elements to search through.
    :param target: The element to find indices of.
    :return: A list of indices where the target is found, or -1 if not found.
    """
    indices = []
    for index, value in enumerate(arr):
        if value == target:
            indices.append(index)
    return indices if indices else -1


def linear_search_first_index(arr, target):
    """
    Get the index of the first occurrence of the target in the array.

    :param arr: List of elements to search through.
    :param target: The element to find the first index of.
    :return: The index of the first occurrence of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def linear_search_last_index(arr, target):
    """
    Get the index of the last occurrence of the target in the array.

    :param arr: List of elements to search through.
    :param target: The element to find the last index of.
    :return: The index of the last occurrence of the target if found, otherwise -1.
    """
    for index in range(len(arr) - 1, -1, -1):
        if arr[index] == target:
            return index
    return -1


# example usage
if __name__ == "__main__":
    sample_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    target_value = 3

    print("Linear Search Index:", linear_search(sample_array, target_value))
    print("Linear Search All Indices:", linear_search_all(sample_array, target_value))
    print("Linear Search First Index:", linear_search_first(sample_array, target_value))
    print("Linear Search Last Index:", linear_search_last(sample_array, target_value))
    print("Linear Search Count:", linear_search_count(sample_array, target_value))
    print("Linear Search Exists:", linear_search_exists(sample_array, target_value))
    print("Linear Search Index:", linear_search_index(sample_array, target_value))
    print("Linear Search All Indices:", linear_search_all_indices(sample_array, target_value))
    print("Linear Search First Index:", linear_search_first_index(sample_array, target_value))
    print("Linear Search Last Index:", linear_search_last_index(sample_array, target_value))
