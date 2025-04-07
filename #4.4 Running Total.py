#constant maximum
MAX = 5

#running total
total = 0.0

#prints instructions to user
print('This program calculates the sum of ', end = '')
print(f'{MAX} numbers you will enter')

#for loop that will iterate 5 times
for counter in range(MAX):

    #ask the user for a number
    number = int(input('Enter: '))

    #print("Total is ", total)

    #the new value of total, is the old value plus the number
    total = total + number

    #print("Total has been changed to", total)

#print total
print(f'The total is {total}')
