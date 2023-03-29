#Bethany Berlage and Grace Anspach
def remove_substring(x,y):
    output=[]
    index=0
    while index<len(x):
        if x[index:index+len(y)]==y:
            index+=len(y)
        else:
            output.append(x[index])
            index+=1
    print("".join(output))

remove_substring("He!ll!o W!orl!d","!")
