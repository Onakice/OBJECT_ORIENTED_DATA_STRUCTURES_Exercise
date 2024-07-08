class funString():

    def __init__(self, string=""):
        self.string = string
    
    def __str__(self):
        return self.string

    def size(self):
        return len(self.string)
    
    def changeSize(self):
        swapped_string = ''.join([char.upper() if char.islower() else char.lower() for char in self.string])
        return swapped_string
    
    def reverse(self):
        reversed_string = self.string[::-1]
        return reversed_string
    
    def deleteSame(self):
        seen = set()
        result = []
        for char in self.string:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)

str_input, func = input("Enter String and Number of Function : ").split()
res = funString(str_input)

if func == "1" :
    print(res.size())
elif func == "2" :
    print(res.changeSize())
elif func == "3" :
    print(res.reverse())
elif func == "4" :
    print(res.deleteSame())