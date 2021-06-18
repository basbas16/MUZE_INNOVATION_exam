alphabet = "abcdefghijklmnopqrstuvwxyz"

def missingLetter(text,cap_check):
    list = []
    for i in range(len(text)):
        if((ord(text[i].lower()) - 96 + 1) != (ord(text[i + 1].lower()) - 96)):
            if(cap_check):
                return alphabet[(ord(text[i].lower()) - 96)].upper()
            else:
                return alphabet[(ord(text[i].lower()) - 96)]


str_list = []
while True:
    text = input("input: ")
    if(text == ""):
        break
    else:
        str_list.append(text)
cap_check = str_list[0].isupper()
print(missingLetter(str_list,cap_check))
