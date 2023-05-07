text = open("encrypted-#B00963042.txt", "r").read()

original_text = []
for x in text:
    if x.isalpha():
        end = ord('A') if x.isupper() else ord('a')
        original_position = (ord(x) - end - (4)) % 26
        x = chr(end + original_position)
        original_text.append(x)
    else:
        original_text.append(" ")
            
decipher = open("decrypted.txt", "w")
decipher.write(str("".join(original_text)))