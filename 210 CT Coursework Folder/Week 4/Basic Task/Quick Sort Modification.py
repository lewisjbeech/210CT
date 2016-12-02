def binary(array, b, c, rangelist=[]):
    #Rangelist is defined as an empty array in the function definiton
    if rangelist == []:
        #only populates rangelist once to lower O(n)
        for i in range(b,c+1,1):
            #Creates the range of values that are being searched for
            rangelist.append(i)
    
    if (len(array)%2 == 0):
        #if the array has an even amount of elements...
        n = int(len(array)/2)
        #defines the mid point
    else:
         #if the array has an odd amount of elements...
        n = int((len(array))/2)
        #defines the midpoint
        
    if (array[n] in rangelist):
        #If the midpoint is in the range of values being searched for
        return True
    elif (n == 0 and array[n] not in rangelist):
        #If the midpoint is the last point as is not a value being searched for
        return False
    elif (c < array[n]):
        #if the largest value in the range of values being found is smaller than the mid point
        del array[n:]
        #removes all the elements in the list after the mid point, these values are no longer being considered
        return binary(array, b, c, rangelist)
        
    elif (array[n] < b):
        #if the smallest value in the range of values being found is larger than the mid point
        del array[:n]
        #removes all the elements in the list before the mid point, these values are no longer being considered
        return binary(array, b, c, rangelist)        
    


numberlist = []
for i in range (int(input("List Size?:"))):
    numberlist.append(int(input("Number: ")))
    #populates a list of interges input by the user

for i in range(1,len(numberlist)):
    x = numberlist[i]
    j = i - 1
    while j >= 0 and numberlist[j] > x:
        temp = numberlist[j+1]
        numberlist[j+1] = numberlist[j]
        numberlist[j] = temp
        j = j - 1
    
    numberlist[j+1] = x

#uses insertion sort to sort the unsorted list of numbers given by the user
    
print(binary(numberlist,int(input("Lower end: ")),int(input("Upper End: "))))
#runs the function and returns the final value, while asking the user for the upper and lower values for the search

Binary(array, b , c)
    if rangelist does not exist
        create rangelist
    n = midpoint of rangelist
    if n in rangelist
        return true
    if n = 0 and n not in rangelist
        return false
    if c < n
        delete larger half of array
        return binary(array,b,c,rangelist)
    if c> n
        delete smaller half of array
        return binary(array,b,c,rangelist)
    
    
