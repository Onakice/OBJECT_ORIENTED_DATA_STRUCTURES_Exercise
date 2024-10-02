def count_freq(nums):
    # Create a dictionary to store the frequency of each number.
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    return freq

def basic_sort(nums):
    # Count frequency of each number
    freq = count_freq(nums)
    
    # Create a list to store unique numbers
    uniq_nums = list(freq.keys())
    
    # Use Bubble Sort to sort based on frequency and number value
    for i in range(len(uniq_nums)):
        for j in range(0, len(uniq_nums) - i - 1):
            # Compare frequency first, then value if frequencies are the same
            if (freq[uniq_nums[j]] < freq[uniq_nums[j + 1]]) or \
               (freq[uniq_nums[j]] == freq[uniq_nums[j + 1]] and uniq_nums[j] < uniq_nums[j + 1]):
                # Swap positions
                uniq_nums[j], uniq_nums[j + 1] = uniq_nums[j + 1], uniq_nums[j]

    return uniq_nums, freq  # Returns unique items and their frequencies

input_data = input("Enter list of numbers: ")
input_list = list(map(int, input_data.split()))

sorted_nums, frequency = basic_sort(input_list)

# Output results
for n in sorted_nums:
    print(f"number {n}, total: {frequency[n]}")
