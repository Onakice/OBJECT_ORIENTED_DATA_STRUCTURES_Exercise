def bubble_sort_recursive (lst, n = None):
    if n is None:
        n = len(lst)

    if n == 1:
        return lst
    
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return bubble_sort_recursive(lst, n - 1)

input_str = input("Enter Input : ")
lst = [int(x) for x in input_str.split(" ")]

sorted_lst = bubble_sort_recursive(lst)

print(sorted_lst)