#Scott Cagnard
#Programming Assignment 1

#Part 1

levels = int(input("Enter a number for how the long the pyramid should go:"))  #Accquire the number of levels of the pyramid from user

building_block = input("Enter a building block to represent the levels of the pyramid:") #Accquire a building block

list = range(1, levels + 1)    #create the range from 1 to levels + 1 and label it as list

for i in list:                   #create a for loop for the range list
    print(building_block * i)   #Print all values in range times the building block in each succesive line


print("\n\n")  # print a couple of blank lines
input("Press any key to continute")
print("\n\n")  # print a couple of blank lines

#Part 2

lev_2 = int(input("Enter a number for how long the pyramid should go:"))   #Accquire the number of levels of the pyramid
build_blck2 = input("Enter a building block to represent the levels of the pyramid:")     #Accquire a building block

y = range(1, lev_2 + 1)   #create the range from 1 to lev_2 + 1 and label it y

for i in (y):               #create a for loop for the y
    s = " " * (lev_2 - i)                   #this decreases the number of blank space each time by 1
    s = s + build_blck2 * (i * 2 - 1)       #this provides the number of building blocks there will be in the row
    print(s)                    #print the result



print("\n\n")  # print a couple of blank lines
input("Press and key to continute")
print("\n\n")  # print a couple of blank lines

#Part 4


x1 = int(input("Enter the number you want to start the range at:"))  #accquire a starting value for the range
x2 = int(input("Enter the number you want to end the range at:"))     #accquire an ending value for the range

while x1 > x2:
    x2 = int(input("Enter a number that is greater than the staring number:"))    #Create a while loop to ensure an appropiate range is given
    

x = range(x1, x2 + 1)     #label the range as x


for i in (x):            #create a for loop for x
    s = " " * (i**2 - 1)             
    s = s + "."         #this provides us to only print the outer points on the edge of the parabola
    print(s)






    
