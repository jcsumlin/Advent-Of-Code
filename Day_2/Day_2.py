with open("day_2_input.txt", "r") as f:
    inputs = f.read()
    inputs = inputs.split("\n")
    inputs = list(filter(None, inputs))
Twos = 0
Threes = 0
for id in inputs:
    incremented_two = False
    incremented_three = False
    for character in id:
        x = id.count(character)
        if x == 2 and incremented_two != True:
            Twos += 1
            incremented_two = True
        elif x == 3 and incremented_three != True:
            Threes += 1
            incremented_three = True
print(str(Twos) +  ' ' +str(Threes))
print("CheckSum: " + str(Twos*Threes))