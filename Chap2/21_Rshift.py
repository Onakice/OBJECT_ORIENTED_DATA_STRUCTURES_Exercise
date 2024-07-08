def Rshift(num, shift):
    return num >> shift

num, sh = input("Enter number and shiftcount : ").split()
print(Rshift(int(num), int(sh)))