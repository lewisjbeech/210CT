def ConsecutiveString(a, pos, string):
    if (string == []):
        string.append(a[pos])
        return ConsecutiveString(a, pos+1, string)
        
    if  (pos != (len(a)-1)):
        
        if (a[pos] > (string[-1])):
            string.append(a[pos])
            return ConsecutiveString(a, pos+1, string)
        else:
            return string
    else:
        if (a[pos] > (string[-1])):
            string.append(a[pos])
            return string
        else:
            return string

numstring = []
longstring=[]

for i in range(int(input("Length: "))):
    numstring.append(int(input("Number: ")))



for i in range(len(numstring)-1):
    
    x = ConsecutiveString(numstring, i, string=[])
    
    
    if (len(x)>len(longstring)):
        longstring = x

print(longstring)

