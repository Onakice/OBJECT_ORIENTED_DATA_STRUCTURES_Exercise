print("*** Fun with Drawing ***")
inp_draw = int(input("Enter input : "))

print("."*(inp_draw-1) + "*" + "."*(2*(inp_draw)-3) + "*" + "."*(inp_draw-1))

for i in range(inp_draw-2, 0, -1):
    print("."*(i) + "*" + "+"*(2*(inp_draw-i-2)+1) + "*" + "."*(2*(i)-1) + "*" + "+"*(2*(inp_draw-i-2)+1) + "*" + "."*(i))

print("*" + "+"*(2*(inp_draw)-3) + "*" + "+"*(2*(inp_draw)-3) + "*")

for i in range(1, 2*inp_draw-2):
    print("."*(i) + "*" + "+"*(2*((2*inp_draw-3)-i)+1) + "*" + "."*(i))

print("."*(2*inp_draw-2) + "*" + "."*(2*inp_draw-2))