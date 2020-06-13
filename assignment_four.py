import cv2

msg = "Digital Forensics Course"
curlen = 0
msglist = list(msg)
binary_num = []
decoded_msg = []

#finding the binary number of each character

for i in range(0,len(msglist)):
    curren_num = ord(msglist[i])
    bin_number = str(bin(curren_num))
    binary_num.append(bin_number[2:])



lenght_char = []
whole_bits = []

for l in range(0,len(binary_num)):
    lenght_char.append(len(binary_num[l]))

for count in range(0,len(binary_num)):
    current_binary = binary_num[count]
    current_binary = list(current_binary)
    whole_bits = whole_bits + current_binary

count = 0
img = cv2.imread('mona.jpg')

row,col,rgb =img.shape
# print(len(whole_bits))

# hiding the text

for i in range(0, row):
    if count == len(whole_bits):
        break
    for j in range(0, col):
        if count == len(whole_bits):
            break
        for k in range(rgb):
            if count == len(whole_bits):
                break
            pixelval = img[i, j, k]
            pixelval = bin(pixelval)
            pixelval = pixelval[2:]
            pixelval = list(pixelval)
            pixelval[-1] = whole_bits[count]
            new_val = ''
            g = 0
            for g in range(0, len(pixelval)):
                new_val = new_val + pixelval[g]
            new_val = int(new_val,2)
            img[i,j,k] = new_val
            count = count + 1


# decrption process

cv2.imwrite('mona_encoded.jpg',img)

newimg = cv2.imread('mona_encoded.jpg')

new_whole_bits = []
new_count = 0
row,col,rgb = newimg.shape
i = 0
j = 0
k = 0
for i in range(0, row):
    if new_count == len(whole_bits):
        break
    for j in range(0, col):
        if new_count == len(whole_bits):
            break
        for k in range(rgb):
            if new_count == len(whole_bits):
                break
            pixelval = img[i, j, k]
            pixelval = bin(pixelval)
            pixelval = pixelval[2:]
            pixelval = list(pixelval)
            new_whole_bits.append(pixelval[-1])

            new_count = new_count + 1

i = 0
g = 0


for i in range(0,len(lenght_char)):
    fichar = lenght_char[i]
    currentstr = ''

    for mas in range(g,fichar+g):
        currentstr = currentstr + new_whole_bits[mas]

    res = int(currentstr, 2)
    character = chr(res)
    decoded_msg.append(character)
    g = fichar + g

i = 0

print("Extracted message is")

for i in range(0,len(decoded_msg)):
    print(decoded_msg[i],end='')




