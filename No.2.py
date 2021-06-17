
def plantTrees(w,l,g):
    tree = 0
    if g == 0:
        return (w * l) - 1
    else:
        len = (w * l) - 1
        strr = []
        for i in range(len):
            strr.append("-")
        for i in range(len):
            if i%(g + 1) == 0:
                strr[i] = "o"
                tree += 1
        for i in range(len):
            # print(7%4)
            if (strr[i] == "o" and (i + g + 1) > len and strr[(i + g + 1) % len] != "o"):
                return 0
            #     # if (i + g + 1) > len(str):
            #
            #     return 0
        return tree


w = int(input())
l = int(input())
g = int(input())

print(plantTrees(w,l,g))
