def insertion_sort_recursive(arr, n=None):
    # Initial call to the function
    if n is None:
        n = len(arr)

    # Base case: If the array size is 1 or less, it's already sorted
    if n <= 1:
        return arr

    # Recursively sort the first n-1 elements
    insertion_sort_recursive(arr, n - 1)

    # Store the last element to be inserted
    last = arr[n - 1]
    j = n - 2

    # Move elements of arr[0..n-1], that are greater than last, to one position ahead
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last  # Insert last in its correct position

    # Split the array into left and right parts
    left_part = arr[:j + 1]  # Sorted part of the array
    right_part = arr[j + 2:n]  # Remaining part of the array

    # Print the steps for each insertion with both left and right parts
    print(f'insert {last} at index {j + 1} : {left_part} {right_part}')

    return arr

# Input and processing
input_data = input("Enter Input : ").strip()
data = list(map(int, input_data.split()))
sorted_data = insertion_sort_recursive(data)

print("sorted")
print(sorted_data)
