def insertion(l, sl=[], i=0):
    # Check if the sorted list (sl) is empty. If it is, initialize it with the first element from the unsorted list (l).
    if len(sl) == 0:
        sl = [l.pop(0)]  # Remove and save the first element from 'l' into 'sl'
    
    # Check if we have reached the end of the sorted list (sl) or if the current element from 'l' is less than or equal to the current element in 'sl' at index 'i'.
    if i == len(sl) or l[0] <= sl[i]:
        # Insert the current element from 'l' into 'sl' at the index 'i'.
        sl.insert(i, l.pop(0))  # Remove the first element from 'l' and insert it into 'sl' at index 'i'
        
        # Print the value inserted and its index, along with the current state of the sorted list (sl)
        print("insert", sl[i], "at index", i, ":", sl, end="")
        
        # If there are no more elements left in 'l', return the sorted list 'sl'
        if len(l) == 0:
            return sl
        
        # Print the remaining elements in 'l' for visibility
        print("", l)
        
        # Recursively call 'insertion' with the updated lists
        return insertion(l, sl)
    else:
        # If the current element in 'sl' is less than the element being processed, move to the next index 'i' and continue the search
        return insertion(l, sl, i + 1)

# Take input from the user and convert it into a list of integers
l = [int(i) for i in input("Enter Input : ").split()]

# Call the insertion function to sort the input list
l = insertion(l)

# Print the sorted list
print("\nsorted")
print(l)