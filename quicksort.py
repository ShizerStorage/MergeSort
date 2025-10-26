def partition_hoare(a, l, r, counts, trace=False):
    pivot_index = (l + r) // 2
    pivot = a[pivot_index]
    if trace:
        print(f"Partitioning a[{l}:{r}] with pivot a[{pivot_index}]={pivot} -> {a[l:r+1]}")
    i = l - 1
    j = r + 1
    while True:
        while True:
            i += 1
            counts['comparisons'] += 1
            if a[i] < pivot:
                continue
            else:
                break
        while True:
            j -= 1
            counts['comparisons'] += 1
            if a[j] > pivot:
                continue
            else:
                break
        if i >= j:
            if trace:
                print(f"Partition index returned: {j}\n")
            return j
        if trace:
            print(f"Swap a[{i}]={a[i]} and a[{j}]={a[j]} ->", end=" ")
        temp = a[i]; a[i] = a[j]; a[j] = temp
        counts['assignments'] += 3
        if trace:
            print(a)

def quicksort_hoare(a, l, r, counts, trace=False):
    if l < r:
        q = partition_hoare(a, l, r, counts, trace=trace)
        quicksort_hoare(a, l, q, counts, trace=trace)
        quicksort_hoare(a, q + 1, r, counts, trace=trace)

if __name__ == "__main__":
    A = [50, 80, 19, 86, 35, 7, 60, 48, 51]

    counts = {'comparisons': 0, 'assignments': 0}
    arr = A[:]

    print("### Quicksort (Hoare) trace on array ###\n")
    quicksort_hoare(arr, 0, len(arr) - 1, counts, trace=True)

    print("Final sorted array:", arr)
    print("Counts:", counts)