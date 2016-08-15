def hash(s):
    h = 7
    letters = "acdegilmnoprstuw"
    for i in range(0,len(s)):
        h = (h * 37 + letters.index(s[i]))
    return h
print hash("lawnmower")

def uhash(number):
    letters = "acdegilmnoprstuw"
    s=""
    while number>7:
        if number%37==0:
            s=letters[0]+s
        else:
            for i in range(0,len(letters)):
                if (number-i)%37==0:
                    s=letters[i]+s
                    break
        number=number/37
    return s
        
print uhash(930846109532517)
