x = int(input("How many eggs each day do the aliens lay? "))
y = int(input("How long does it take for the eggs to hatch? "))
z = int(input("How many days do the aliens have to breed?" ))
#Takes all the variables and assigns them as integers
aliens = []
n = 0
while (n < z) is True:
    aliens.append(0)
    n = n+ 1

aliens[0] = 1

#creates a list of thirty elements and sets the initial invasion, 1 alien

n = 1 

while (n < z):
    aliens[n] = (aliens[n-1] + (aliens[n-y])*x)

    n = n + 1

#uses the formula (n = (n-1) + x(n-y)) to calculate the amount of aliens
    
print("{} {} {}, {}".format("There will be", aliens[z-1], "aliens", "you're dooooooooomed!"))
