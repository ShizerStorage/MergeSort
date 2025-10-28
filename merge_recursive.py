def merge(left, right, counts):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        counts['comparisons'] += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            counts['assignments'] += 1
            i += 1
        else:
            merged.append(right[j])
            counts['assignments'] += 1
            j += 1

    # Add remaining elements
    while i < len(left):
        merged.append(left[i])
        counts['assignments'] += 1
        i += 1

    while j < len(right):
        merged.append(right[j])
        counts['assignments'] += 1
        j += 1

    return merged


def merge_sort(arr, counts=None):
    if counts is None:
        counts = {'comparisons': 0, 'assignments': 0}

    if len(arr) <= 1:
        return arr, counts

    mid = len(arr) // 2
    left, counts = merge_sort(arr[:mid], counts)
    right, counts = merge_sort(arr[mid:], counts)

    merged = merge(left, right, counts)
    return merged, counts


# Example usage
if __name__ == "__main__":
    arr = [38, 27, 70, 23, 7, 44]
    sorted_arr, counts = merge_sort(arr)
    print("Sorted array:", sorted_arr)
    print("Counts:", counts)

