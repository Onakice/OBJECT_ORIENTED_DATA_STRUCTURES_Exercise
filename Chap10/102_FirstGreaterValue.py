def find_first_greater(left, right):
    left.sort()
    for i in right:
        greater_values = [x for x in left if x > i]
        if greater_values:
            print(min(greater_values))
        else:
            print("No First Greater Value")

inp = input("Enter Input : ").split("/")

left = list(map(int, inp[0].split()))
right = list(map(int, inp[1].split()))

find_first_greater(left, right)