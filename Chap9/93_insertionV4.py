def custom_sort(arr):
    # สร้าง dictionary เพื่อนับจำนวนครั้งของแต่ละเลข
    freq_dict = {}
    for i in arr:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    result = []
    # ดึงค่าจาก dict โดยเก็บตามลำดับเดิม (ตามที่ปรากฏครั้งแรกใน input)
    seen = set()  # set เพื่อเก็บตัวเลขที่เจอแล้ว
    for num in arr:
        if num not in seen:
            result.append((num, freq_dict[num]))
            seen.add(num)

    def bubble_sort(data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                # ตรวจเงื่อนไขการจัดเรียง: เรียงจากจำนวนซ้ำมากไปน้อย
                if data[j][1] < data[j + 1][1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

    bubble_sort(result)

    for num, count in result:
        print(f"number {num}, total: {count}")

input_numbers = list(map(int, input("Enter list  of numbers: ").split()))
custom_sort(input_numbers)