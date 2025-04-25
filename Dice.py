characters = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM"
encryption = "1234567890}{][|!§$%&/()=?`´^°*+~#'-_:.;,<>@€µ"

character_without_encryption = input("Enter a character to encrypt: ")
character_with_encryption = input("ENter a encryption to decrypt: ")
output = ""
output2 = ""
for i in range(len(character_without_encryption)):
    if character_without_encryption[i] in characters:
        output += encryption[characters.index(character_without_encryption[i])]
    else:
        output += character_without_encryption[i]

print(output)


for i in range (len(character_with_encryption)):
    if character_with_encryption [i] in encryption:
        output2 += characters[encryption.index(character_with_encryption[i])]
    else:
        output2 += character_with_encryption
print(output2)