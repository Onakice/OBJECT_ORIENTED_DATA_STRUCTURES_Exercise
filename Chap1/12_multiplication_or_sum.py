print("*** multiplication or sum ***")
num1, num2 = map(int, input("Enter num1 num2 : ").split())
result = 0
if num1 * num2 > 1000 :
    result = num1 + num2
else:
    result = num1 * num2
print(f"The result is {result}")