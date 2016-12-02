def matrixAdd(A,B):
    if (A.shape == B.shape) is False:        
        return 'This cannot be done, the matrix are of the wrong dimensions'
    #Two Matrix can only be added if they are of the same dimensions.
    y = 0
    x = 0

    a = A.shape
    b = a[1]
    c = a[0]
    C = zeros(shape=(a))
    #Defines all of the variables needed, as well as an empty matrix.

    while (y < c) is True:
        #cycles down the two arrays
        while (x < b) is True:
            #cycles across the two arrays

             C[y,x] = A[y,x] + B[y,x]
             #adds the values at the same co-ords of each matrix

             x = x + 1

        y = y + 1
        x = 0
    return C
    #returns the calculated matrix C

def matrixSub(A,B):
    if (A.shape == B.shape) is False:
        return 'This cannot be done, the matrix are of the wrong dimensions'
    #Two Matrix can only be subtracted if they are of the same dimensions.
    y = 0
    x = 0

    a = A.shape
    b = a[1]
    c = a[0]
    C = zeros(shape=(a))
    #Defines all of the variables needed, as well as an empty matrix.

    while (y < c) is True:
        #cycles down the two arrays
        while (x < b) is True:
            #cycles across the two arrays

            C[y,x] = A[y,x] - B[y,x]
            #subtracts the values at the same co-ords of each matrix
            x = x + 1

        y = y + 1
        x = 0
    return C
    #returns the calculated array C

def matrixMult(A,B):
    y = 0
    x = 0
    n = 0
    tempnum = 0

    a = A.shape
    z = a[1]
    a = a[0]

    b = B.shape
    w = b[0]
    b = b[1]
    
    if (z == w) is False:       
        return 'This cannot be done, the matrix are of the wrong dimensions'
    C = zeros(shape=(b,a))
    # #Defines all of the variables needed, as well as an empty matrix.

    while (y < a) is True:
        #cycles down the two arrays
        while (x < b) is True:
            #cycles across the two arrays
            while n < z:
                #calculates the dot product
                tempnum = A[y,n] * B[n,x] + tempnum
                n = n + 1

            C[y,x] = tempnum
            #Assigns the dot product to the value in the results Matrix C

            tempnum = 0
            n = 0
            x = x + 1
            #resets the valuses ready for another dot product
            #cycles across the x axis of the second matrix

        y = y + 1
        x = 0
        #resets the valuses ready for another dot product
        #cycles across the y axis of the second matrix

    return C

from numpy import *

a = matrix(input("a: "))

b = matrix(input("b: "))

print("Add", '\n', matrixAdd(a,b))
print("Subtract", '\n' ,matrixSub(a,b))
print("Multiply", '\n' ,matrixMult(a,b))







