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
    
    # Sort by count (from highest to lowest)
    items.sort(key=lambda x: x[1], reverse=True)
    
    # Group items by count
    grouped = {}
    for number, total in items:
        if total not in grouped:
            grouped[total] = []
        grouped[total].append(number)

    # Create a sorted result list
    sorted_items = []
    for total in sorted(grouped.keys(), reverse=True):  # Sort total from high to low
        numbers = grouped[total]
        if len(numbers) == 2:
            # Sort numbers from low to high if there are only two
            numbers.sort()
        else:
            # Sort numbers from high to low if there are more than two
            numbers.sort(reverse=True)
        sorted_items.extend((number, total) for number in numbers)
    
    return sorted_items

input_numbers = input("Enter list  of numbers: ")
numbers = list(map(int, input_numbers.split()))

count_dict = count_numbers(numbers)
sorted_items = custom_sort(count_dict)

for number, total in sorted_items:
    print(f"number {number}, total: {total}")
