with open("day_1.txt", "r") as f:
    inputs = f.read()
    inputs = inputs.split("\n")
    inputs = list(filter(None, inputs))
int_list = []
total = 0
for x in inputs:
    int_list.append(int(x))
for x in int_list:
    total += x

