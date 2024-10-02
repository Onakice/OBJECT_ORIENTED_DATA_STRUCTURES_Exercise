# ฟังก์ชันสำหรับเรียงลำดับตามขนาดของ subset และถ้าขนาดเท่ากันให้เรียงตัวเลขจากน้อยไปมาก
def bubble_sort_subsets(subsets):
    n = len(subsets)
    for i in range(n):
        for j in range(0, n-i-1):
            # ถ้า subset ปัจจุบันใหญ่กว่า subset ถัดไป ให้สลับที่
            if len(subsets[j]) > len(subsets[j+1]):
                subsets[j], subsets[j+1] = subsets[j+1], subsets[j]
            # ถ้าขนาดเท่ากัน ให้เรียงตัวเลขภายใน subset จากน้อยไปมาก
            elif len(subsets[j]) == len(subsets[j+1]):
                if not is_sorted(subsets[j]):
                    bubble_sort(subsets[j])
                if not is_sorted(subsets[j+1]):
                    bubble_sort(subsets[j+1])
                if subsets[j] > subsets[j+1]:
                    subsets[j], subsets[j+1] = subsets[j+1], subsets[j]

# ฟังก์ชันเช็คว่าชุดตัวเลขเรียงลำดับแล้วหรือไม่
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# ฟังก์ชันสำหรับเรียงลำดับภายใน subset จากน้อยไปมาก
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# ฟังก์ชันหาทุก subset ที่ผลรวมเท่ากับเป้าหมาย
def find_subset_sum(arr, target):
    result = []
    def find_subsets(i, subset):
        if sum(subset) == target:
            result.append(subset.copy())
        if i >= len(arr):
            return
        # สำรวจสองทางเลือก: รวมค่า arr[i] และไม่รวม
        find_subsets(i + 1, subset + [arr[i]])  # รวมค่า arr[i]
        find_subsets(i + 1, subset)             # ไม่รวมค่า arr[i]
    
    find_subsets(0, [])
    return result

def process_input(data):
    # แยกข้อมูลออกเป็นผลรวมที่ต้องการและ list ของจำนวนเต็ม
    target_str, arr_str = data.split('/')
    target = int(target_str)
    arr = list(map(int, arr_str.split()))
    
    # หาทุก subset ที่ผลรวมเท่ากับเป้าหมาย
    subsets = find_subset_sum(arr, target)
    
    # ถ้าไม่มี subset ที่ตรงกับเป้าหมาย ให้พิมพ์ "No Subset"
    if not subsets:
        print("No Subset")
    else:
        # เรียงลำดับ subset ตามขนาดและตัวเลข
        bubble_sort_subsets(subsets)
        # พิมพ์แต่ละ subset ที่เจอ
        for subset in subsets:
            print(subset)

# รับ input
input_data = input("Enter Input: ")
process_input(input_data)