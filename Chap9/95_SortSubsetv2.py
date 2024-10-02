# ฟังก์ชันสำหรับหา subset ทั้งหมดของ list ที่มีผลรวมเท่ากับ target
def find_subsets_with_sum(nums, target):
    subsets = []
    
    def find_subsets(path, index, current_sum):
        # ถ้าผลรวมเท่ากับ target ให้เพิ่ม subset ลงในผลลัพธ์
        if current_sum == target:
            # เพิ่มเฉพาะ subset ที่ยังไม่ถูกเพิ่มเข้าไปใน subsets
            if path not in subsets:
                subsets.append(path)
        if index == len(nums):
            return
        # ลองเอาตัวเลข index ปัจจุบันเข้าไปใน subset
        find_subsets(path + [nums[index]], index + 1, current_sum + nums[index])
        # ลองไม่เอาตัวเลข index ปัจจุบันเข้าไปใน subset
        find_subsets(path, index + 1, current_sum)
    
    find_subsets([], 0, 0)
    return subsets

# ฟังก์ชัน Bubble Sort สำหรับการเรียงลำดับ list จากน้อยไปมาก
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# ฟังก์ชันสำหรับเรียง subset ทั้งหมด
# 1. เรียงตามขนาด subset
# 2. ถ้าขนาดเท่ากัน ให้เรียงตัวเลขภายใน subset
def sort_subsets(subsets):
    # ใช้ bubble_sort สำหรับแต่ละ subset
    for subset in subsets:
        bubble_sort(subset)

    # เรียง subsets ตามขนาด และถ้าขนาดเท่ากันก็เรียงตามค่าของตัวเลข
    n = len(subsets)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(subsets[j]) > len(subsets[j+1]):
                subsets[j], subsets[j+1] = subsets[j+1], subsets[j]
            elif len(subsets[j]) == len(subsets[j+1]):
                if subsets[j] > subsets[j+1]:
                    subsets[j], subsets[j+1] = subsets[j+1], subsets[j]

# เริ่มต้นการทำงานของโปรแกรม
input_data = input("Enter Input : ")
target_str, nums_str = input_data.split('/')

# แปลง input เป็น target (int) และ nums (list ของ int)
target = int(target_str)
nums = list(map(int, nums_str.split()))

# หาชุดย่อยที่มีผลรวมเท่ากับ target
subsets = find_subsets_with_sum(nums, target)

# ถ้ามี subset ให้ทำการเรียงลำดับ
if subsets:
    sort_subsets(subsets)
    # แสดงผลลัพธ์
    for subset in subsets:
        print(subset)
else:
    print("No Subset")
