def find_triplets_with_sum(arr, target):
    arr.sort()
    triplets = []
    n = len(arr)
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                triplet = [arr[i], arr[left], arr[right]]
                if triplet not in triplets:
                    triplets.append(triplet)
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return triplets

while True:
    input_list = input("Enter Your List : ")
    arr = list(map(int, input_list.split()))

    if len(arr) >= 3:
        break
    else:
        print("Array Input Length Must More Than 2")
        break

target_sum = 5
result = find_triplets_with_sum(arr, target_sum)
# print(result)

if result:
    print(result)