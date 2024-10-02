def can_pack(weights, max_weight, k):
    current_weight = 0
    box_count = 1

    for weight in weights:
        if current_weight + weight > max_weight:
            box_count += 1
            current_weight = weight
            if box_count > k:
                return False
        else:
            current_weight += weight

    return True

def find_minimum_max_weight(weights, k):
    left = max(weights)  # น้ำหนักน้อยสุดคือ น้ำหนักของสินค้าที่หนักที่สุด
    right = sum(weights)  # น้ำหนักมากสุดคือ น้ำหนักรวมของสินค้าทั้งหมด
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_pack(weights, mid, k):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

input_data = input("Enter Input : ")
weights_str, k_str = input_data.split('/')
weights = list(map(int, weights_str.split()))
k = int(k_str)

min_weight = find_minimum_max_weight(weights, k)

print(f"Minimum weigth for {k} box(es) = {min_weight}")
