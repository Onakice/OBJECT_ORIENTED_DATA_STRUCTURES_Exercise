def calculateLoveScore(my, your):
    decode(my, your)
    total_score = 0
    for i in range(len(my)) :
        if my[i] == your[i]:
            # print(my[i])
            # print(your[i])
            pass

def decode(act, loc):
    act_str = ""
    loc_str = ""

    for a in act:
        if a == '0':
            act_str += "Eat "
        elif a == '1':
            act_str += "Game "
        elif a == '2':
            act_str += "datastruc(Learn) "
        elif a == '3':
            act_str += "Movie "

    for l in loc:
        if l == '0':
            loc_str += "Res. "
        elif l == '1':
            loc_str += "ClassR. "
        elif l == '2':
            loc_str += "SuperM. "
        elif l == '3':
            loc_str += "Home "
    
    act_str = act_str.strip()
    loc_str = loc_str.strip()

    return act_str, loc_str

# def decode(act, loc):
#     act_list = []
#     loc_list = []
#     print("in decode")

#     for a in act:
#         if a == '0':
#             act_list.append("Eat")
#         elif a == '1':
#             act_list.append("Game")
#         elif a == '2':
#             act_list.append("datastruc(Learn)")
#         elif a == '3':
#             act_list.append("Movie")

#     for l in loc:
#         if l == '0':
#             loc_list.append("Res.")
#         elif l == '1':
#             loc_list.append("ClassR.")
#         elif l == '2':
#             loc_list.append("SuperM.")
#         elif l == '3':
#             loc_list.append("Home")
    
#     return act_list, loc_list



inps = input("Enter Input : ").split(',')

# print(inps)

day_list_my = []
day_list_your = []

for day in inps:
    day_of_two_p = day.split()
    day_list_my.append(day_of_two_p[0])
    day_list_your.append(day_of_two_p[1])
    
    # day_list_my_act, day_list_my_location = day_list_my.split(':')
my_act = []
my_loc = []

for day in day_list_my:
    temp = day.split(':')
    # my_act.append(day)
    my_act.append(temp[0])
    my_loc.append(temp[1])

print(f"my_act : {my_act}")
print(f"my_loc : {my_loc}")

act_list, loc_list = decode(my_act, my_loc)
# print(f"My   Activity:Location = {act_list}:{loc_list}")
# print(f"My   Activity:Location = {', '.join([f'{act}:{loc}' for act, loc in zip(act_list, loc_list)])}")
# print(f"Your Activity:Location = {', '.join([f'{act}:{loc}' for act, loc in zip(act_list, loc_list)])}")

my = ""

# for i in range(len(act_list)):
#     act += ' '.join([f'{act_list[i]}:{loc_list[i]}'])

my = ' '.join([f'{act_list[i]}:{loc_list[i]}' for i in range(len(act_list))]) 
my = ' '.join([f'{act_list[i]}:{loc_list[i]}' for i in range(len(act_list))])
print(f"act : {my}")

result = calculateLoveScore(day_list_my, day_list_your)

# print(day_list_my)
# print(f"My : {day_list_my}")


# convert list to str eiei
for i in day_list_my :
    day_list_my_str = ', '.join(day_list_my)
    day_list_your_str = ', '.join(day_list_your)

# print(f"My : {day_list_my_str}")

# print(f"My_Act : {day_list_my_act}")
# print(f"My_Location : {day_list_my_location}")



# print(f"Your : {day_list_your}")
# print(f"Your : {day_list_your_str}")