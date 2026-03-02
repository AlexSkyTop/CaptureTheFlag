with open("rev_this", "rb") as f:
    data = f.read()

flag = []
for i in range(8):
    flag.append(data[i])

for i in range(8, 24):
    if i % 2 == 0: # indices pairs → on inverse +5 => -5
        orig = data[i] - 5
    else:  # indices impairs → on inverse -2 => +2
        orig = data[i] + 2
    flag.append(orig)

flag_bytes = bytes(flag)
print("Flag original :", flag_bytes.decode() + "}")