#Bethany Berlage and Grace Anspach

def replace_substring(x,y,z):
    output=[]
    index=0
    while index<len(x):
        if x[index:index+len(y)]==y:
            index+=len(y)
            output.append(z)
        else:
            output.append(x[index])
            index+=1
    print("".join(output))

replace_substring("He!ll!o W!orl!d","!","?")
