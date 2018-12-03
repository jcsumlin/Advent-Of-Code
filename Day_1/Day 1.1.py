with open("day_1.txt", "r") as f:
    inputs = f.read()
    inputs = inputs.split("\n")
    inputs = list(filter(None, inputs))
frequencies = set()
freq = 0
list_o_ints = []
for x in inputs:
    list_o_ints.append(int(x))


while True:
    for x in list_o_ints:
        freq += x
        if freq in frequencies:
            print("Freq: %s"%freq)
            exit()
        else:
            frequencies.add(freq)
