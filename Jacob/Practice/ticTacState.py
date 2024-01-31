binaryList = []
octal = "0116777"

for ch in octal: 
    binaryList.append(bin(int(ch))[2:])

binaryString = "".join(binaryList)

print(binaryString)
