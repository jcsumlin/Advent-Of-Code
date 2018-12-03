from difflib import SequenceMatcher


with open("day_2_input.txt", "r") as f:
    inputs = f.read()
    inputs = inputs.split("\n")
    inputs = list(filter(None, inputs))

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


max_ratio = 0.0
similar_string_a = ""
similar_string_b = ""

for x in inputs:
    index = inputs.index(x)
    for i in range(1, len(inputs)):
        try:
            next = inputs[index+i]
            ratio = similar(x, next)
            if ratio > max_ratio:
                max_ratio = ratio
                similar_string_a = x
                similar_string_b = next
        except:
            pass


u = zip(similar_string_a, similar_string_b)
u = list(u)
final_string = ""
for i, j in u:
    if i == j:
        final_string += i
print(final_string)