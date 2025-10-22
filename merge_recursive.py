def merge_recursive(left_list, right_list, counts, trace=False):
    i = 0
    j = 0
    result = []
    if trace:
        print(f"Merging (recursive) {left_list} + {right_list}")
    while i < len(left_list) and j < len(right_list):
        counts['comparisons'] += 1
        if left_list[i] <= right_list[j]:
            result.append(left_list[i])
            counts['assignments'] += 1
            i += 1
        else:
            result.append(right_list[j])
            counts['assignments'] += 1
            j += 1
    while i < len(left_list):
        result.append(left_list[i])
        counts['assignments'] += 1
        i += 1
    while j < len(right_list):
        result.append(right_list[j])
        counts['assignments'] += 1
        j += 1
    if trace:
        print(f" -> {result}\n")
    return result


def merge_sort_recursive(a, counts=None, trace=False):
    if counts is None:
        counts = {'comparisons': 0, 'assignments': 0}
    n = len(a)
    if n <= 1:
        return a, counts
    mid = n // 2
    left_half, counts = merge_sort_recursive(a[:mid], counts, trace=trace)
    right_half, counts = merge_sort_recursive(a[mid:], counts, trace=trace)
    merged = merge_recursive(left_half, right_half, counts, trace=trace)
    return merged, counts


if __name__ == "__main__":
    original_array = [50, 80, 19, 86, 35, 7, 60, 48, 51]

    print("### Recursive merge sort (trace=True) ###\n")
    arr_rec = original_array[:]
    sorted_rec, counts_rec_trace = merge_sort_recursive(arr_rec, trace=True)
    print("Recursive counts (with trace):", counts_rec_trace)
    print("Sorted array (recursive):", sorted_rec)
