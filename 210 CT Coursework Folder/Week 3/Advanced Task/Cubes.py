def Tower(a, b, n=0, Colour=0, Size=999):
    #values colour and size default to values if no values are given
    
    if (len(a) == 1) is True:
        x = int(a.pop())
        y = b.pop()
        #pops off the end element in the list to compare them
        if ((x < Size) and (y != Colour)):
            return (str(x)+y)
        #If the block is both smaller and off a different colour
        else:
            return 
    #base case to end the recursion, happens only once every other element from a and b has been popped
    elif n == 0:
        x = int(a.pop())
        y = b.pop()
        return (str(x)+y), Tower(a, b, n+1, y, x)
        #if on the first iteration itll will simply add the largest cube to the bottom of the stack
    else:
        x = int(a.pop())
        y = b.pop()
        if ((x < Size) and (y != Colour)):
            return (str(x)+y), Tower(a, b, n+1, y, x)
        #For each cube if it follows the criteria adds it to the top of the tower of cubes
        else:
            return Tower(a, b, n+1, Colour, Size)
Size = []
Colour = []
for i in range(0,5):
    z = input("Block size/Colour: ")
    x = z[0]
    y = z[1]
    Size.append(x)
    Colour.append(y)
#creates a list of the blocks colours and sizes input from the user

for i in range(1,len(Size)):
    x = Size[i]
    j = i - 1
    while j >= 0 and Size[j] > x:
        temp = Size[j+1]
        Size[j+1] = Size[j]
        Size[j] = temp
        temp = Colour[j+1]
        Colour[j+1] = Colour[j]
        Colour[j] = temp
        j = j - 1
    
    Size[j+1] = x

#insertion sort to sort the boxes into numerical order

print("Blocks in Ascending order", Tower(Size, Colour))
            



    
    
