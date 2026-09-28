def merge_two_lists(list_a, list_b):
    result = []
    i = j = 0
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            result.append(list_a[i])
            i += 1
        else:
            result.append(list_b[j])
            j += 1
    
    if i < len(list_a):
        result.extend(list_a[i:])
    elif j < len(list_b):
        result.extend(list_b[j:])

    return result


def main(list_a, list_b, c):
    list_ab = merge_two_lists(list_a, list_b)
    return merge_two_lists(list_ab, c)

assert (main([1, 4, 7], [2, 5, 8], [3, 6, 9])
                     == [1, 2, 3, 4, 5, 6, 7, 8, 9])
assert main([1, 2], [3, 4, 5, 6, 7], [8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert main([], [], [1, 2, 3]) == [1, 2, 3]
assert main([5], [1], [3]) == [1, 3, 5]
print("all passed")
