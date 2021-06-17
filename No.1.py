import math

text = input("input: ")

def convert(text):
    if(text.find("°C") != -1):
        c_temp = int(text[0:text.find("°")])
        f_temp = (c_temp * 9 / 5) + 32
        if(f_temp > 0):
            return str(math.floor(f_temp))+"°F"
        else:
            return str(math.ceil(f_temp))+"°F"
    elif(text.find("°F") != -1):
        f_temp = int(text[0:text.find("°")])
        c_temp = (f_temp - 32) * 5 / 9
        if(c_temp > 0):
            return str(math.floor(c_temp))+"°C"
        else:
            return str(math.ceil(c_temp))+"°C"
    else:
        return "error"

print(convert(text))
