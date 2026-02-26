
word = input("Enter the word : ")

big = "".join(f"{ord(c):02X}" for c in word)
little = "".join(f"{ord(c):02X}" for c in word[::-1])

print("Little:", little)
print("Big:", big)