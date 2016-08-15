def hash(s):
    h = 7
    letters = "acdegilmnoprstuw"
    for i in range(0,len(s)):
        h = (h * 37 + letters.index(s[i]))
    return h
print hash("lawnmower")

def uhash(number):
    #Characters that can be used
    letters = "acdegilmnoprstuw"
    s=""
    while number>7:
        #To check if it is the first character in 'letters'
        if number%37==0:
            s=letters[0]+s
        else:
            #find the next character of string
            for i in range(0,len(letters)):
                if (number-i)%37==0:
                    s=letters[i]+s
                    break
        number=number/37
    return s
        
print uhash(930846109532517)
