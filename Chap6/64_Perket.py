def mindif(inp):
    n = len(inp)
    mindif = float('inf')

    for i in range(1, 1 << n):
        sour = 1
        bitter = 0
        for j in range(n):
            if i & (1 << j):
                s, b = inp[j]
                sour *= s
                bitter += b
        diff = abs(sour - bitter)
        if diff < mindif:
            mindif = diff

    return mindif

inps = input("Enter Input : ")

inp = [tuple(map(int, item.split())) for item in inps.split(',')]

result = mindif(inp)
print(result)