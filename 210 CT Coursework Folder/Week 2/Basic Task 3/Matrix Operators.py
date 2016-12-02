MATRIXADD(A,B)
    if shape of A  !=  Shape of B
        return matrix the wrong size

    y <- 0
    x <- 0

    create matrix C in same dimensions as A and B

    while y < y dimensions of A and B
        while x < x dimensions of A and B
            C(x,y) = A(x,y) + B(x,y)

            x <- x + 1

        y <- y + 1
        x <- 0

    return C

MATRIXSUBTRACT(A,B)
    if shape of A !=  Shape of B
        return matrix the wrong size

    y <- 0
    x <- 0

    create matrix C in same dimensions as A and B

    while y < y dimensions of A and B
        while x < x dimensions of A and B
            C(x,y) = A(x,y) - B(x,y)

            x <- x + 1

        y <- y + 1
        x <- 0

    return C

MATRIXMULTIPLICATION(A,B)
    y <- 0
    x <- 0
    n <- 0

    if (x dimension of A) != y dimension of B
        return matrix are of wrong size

    create empty matrix C

    while y < y dimensions of A
        while x < x dimensions of  B
            while n < x dimension of A
                temp <- A(y,n)*B(n,x)

            c(y,x) <- temp
            temp <- 0
            x <- x + 1
            n <- 0
        y <- y + 1
        x <- 0

    return C


A = MATRIXMULT(B,C) - 2 * (MATRIXADD(B,C))
O(n^3 + 6n^2 + 4n + 7)

    
