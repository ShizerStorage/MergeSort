def merge_iterative(a, left, mid, right, counts, trace=False):
    it1 = 0
    it2 = 0
    result = [None] * (right - left)
    if trace:
        print(f"Merging segments a[{left}:{mid}] and a[{mid}:{right}] -> {a[left:mid]} + {a[mid:right]}")
    while left + it1 < mid and mid + it2 < right:
        counts['comparisons'] += 1
        if a[left + it1] <= a[mid + it2]:
            result[it1 + it2] = a[left + it1]
            counts['assignments'] += 1
            it1 += 1
        else:
            result[it1 + it2] = a[mid + it2]
            counts['assignments'] += 1
            it2 += 1
    while left + it1 < mid:
        result[it1 + it2] = a[left + it1]
        counts['assignments'] += 1
        it1 += 1
    while mid + it2 < right:
        result[it1 + it2] = a[mid + it2]
        counts['assignments'] += 1
        it2 += 1
    for i in range(it1 + it2):
        a[left + i] = result[i]
        counts['assignments'] += 1
    if trace:
        print(f"Result placed at a[{left}:{right}] -> {a[left:right]}\n")


def merge_sort_iterative(a, trace=False):
    n = len(a)
    counts = {'comparisons': 0, 'assignments': 0}
    i = 1
    if trace:
        print("Starting iterative merge sort, initial array:", a, "\n")
    while i < n:
        j = 0
        while j < n:
            left = j
            mid = min(j + i, n)
            right = min(j + 2 * i, n)
            if mid < right:
                merge_iterative(a, left, mid, right, counts, trace=trace)
            j += 2 * i
        i *= 2
        if trace:
            print(f"After block size {i//2}, array = {a}\n")
    if trace:
        print("Iterative merge sort finished. Sorted array:", a, "\n")
    return counts, a

if __name__ == "__main__":
    original_array = [50, 80, 19, 86, 35, 7, 60, 48, 51]

    print("### Iterative merge sort (trace=True) ###\n")
    arr_iter = original_array[:]
    counts_iter_trace, sorted_iter = merge_sort_iterative(arr_iter, trace=True)
    print("Iterative counts:", counts_iter_trace)
    print("Sorted array (iterative):", sorted_iter)