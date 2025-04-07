#start at 0
n= 0

#keep looping while n is less than 100
while n < 100:
    print(n)

    #if n does equal 5, break out of the loop
    #the loop will stop iterating and go to the next line of code
    if n == 5:
        break

    #add 1 to n
    n += 1

#show when the loop stopped
print(f'The loop stopped and n is {n}')
