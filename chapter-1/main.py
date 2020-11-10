def binary_search(array, search):
    low = 0
    high = len(array) - 1

    count = 0

    while low <= high:
        mid = int((low + high) / 2)
        guess = array[mid]

        count += 1

        if search == guess:
            print(count)
            return mid
        elif search < guess:
            high = mid - 1
        else:
            low = mid + 1
    else:
        print(count)
        return None


assert None == binary_search([0, 1, 2, 3], 7)
assert binary_search(range(129), 4) == 4
assert binary_search(range(257), 4) == 4
assert binary_search([1, 2, 3, 4, 5], 4) == 3
assert binary_search([1, 2, 3, 4, 5], 3) == 2
assert binary_search([1, 2, 3, 4, 5], 1) == 0
