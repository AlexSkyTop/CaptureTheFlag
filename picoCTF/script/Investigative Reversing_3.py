def extract_flag(encoded_bmp):
    with open(encoded_bmp, "rb") as f:
        data = f.read()
    header_size = 0x2d3
    flag_chars = []
    index = header_size
    for i in range(100):
        if i % 2 == 1:
            flag_chars.append(chr(data[index]))
            index += 1
        else:
            bits = [(data[index + j] & 1) for j in range(8)]
            char_value = sum((bits[j] << j) for j in range(8))
            flag_chars.append(chr(char_value))
            index += 8
    return "".join(flag_chars)

flag = extract_flag("encoded.bmp")
flag = [ord(i) for i in flag]
flag = "".join([chr(i) for i in flag if 32<i<126 and i!=96 and i!=64])
print("Flag:", flag)

# By AlexSkyTop
