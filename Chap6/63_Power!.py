def powerer(num, power):
    # if power <= 1:
    #     return print("Hee")
    # power(num - 1)
    # print(num, end=' ')

    if power == 0:
        return 1
    if power == 1:
        return num
    
    return num * powerer(num, power - 1)


inp = input("Enter Input a b : ")
num, power = map(int, inp.split())

result = powerer(num, power)
print(result)