def checkCode (first_str,last_str):
    return last_str - first_str
    
def getPassCode (secret, lists):
    listed = []
    for i in range(len(lists)) :
        listey = lists[i] + secret
        listed.append(listey)
    return listed

def translateAscii (lists):
    translated = []

    for trans in range(len(lists) - 2):
        translatey = chr(lists[trans])
        translated.append(translatey)
        print(translated)
    

input_string = input("Enter code,hint : ")

char_list = list(input_string)

ascii_list = [ord(char) for char in char_list]

secretCode = checkCode(ascii_list[0], ascii_list[-1])

unlockCode = getPassCode(secretCode, ascii_list)

lastStr = translateAscii (unlockCode)