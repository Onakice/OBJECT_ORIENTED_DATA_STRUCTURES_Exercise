def insertion_sort(arr):
    """Sort the array using insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def find_median(sorted_arr):
    """Find the median of the sorted array."""
    n = len(sorted_arr)
    if n % 2 == 0:
        median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        median = sorted_arr[n // 2]
    return median

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "MinHeap and MaxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:
    l = list(map(int, l))
    sorted_list = []

    for num in l:
        # Insert num into sorted_list
        sorted_list.append(num)

        # Create a copy of the sorted list for sorting
        temp_sorted_list = sorted_list.copy()
        insertion_sort(temp_sorted_list)

        # Find median after each insertion
        median = find_median(temp_sorted_list)

        # Prepare the output format
        print(f"list = {sorted_list} : median = {median:.1f}")
