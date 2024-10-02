def count_numbers(numbers):
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    return count_dict

def custom_sort(count_dict):
    # Convert the dictionary into a list of tuples and sort it
    items = list(count_dict.items())
    # Sort by count (from highest to lowest) and by number (from lowest to highest) if counts are equal
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if (items[j][1] < items[j + 1][1]) or (items[j][1] == items[j + 1][1] and items[j][0] > items[j + 1][0]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


input_numbers = input("Enter list  of numbers: ")
numbers = list(map(int, input_numbers.split()))

count_dict = count_numbers(numbers)
sorted_items = custom_sort(count_dict)

for number, total in sorted_items:
    print(f"number {number}, total: {total}")
