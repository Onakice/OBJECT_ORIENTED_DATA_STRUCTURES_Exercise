def odd_even(data_type, data, mode):
    if data_type == 'S':
        data = list(data)
    elif data_type == 'L':
        data = data.split()
    else:
        return "Invalid data type. Use 'S' for string or 'L' for list."

    if mode == 'Odd' and data_type == 'S':
        return ''.join([data[i] for i in range(len(data)) if i % 2 == 0])
    elif mode == 'Even' and data_type == 'S':
        return ''.join([data[i] for i in range(len(data)) if i % 2 != 0])
    elif mode == 'Odd' and data_type == 'L':
        return [data[i] for i in range(len(data)) if i % 2 == 0]
    elif mode == 'Even' and data_type == 'L':
        return [data[i] for i in range(len(data)) if i % 2 != 0]
    else:
        return "Invalid mode. Use 'Odd' for odd positions or 'Even' for even positions."
    
print("*** Odd Even ***")

input_str = input("Enter Input : ")

input_list = input_str.split(',')

if len(input_list) == 3:
    data_type = input_list[0]
    data = input_list[1]
    mode = input_list[2]

    result = odd_even(data_type, data, mode)
    print(result)
else:
    print("Invalid input format. Please enter in the format: data_type,data,mode")