#4.4 X
#4.5 X
#4.7
#4.8 
#while vs for
#how to find days hours minutes seconds from given seconds



MAX = 5

total = 0.0

print('This program calculates the sum of ', end = '')
print(f'{MAX} numbers you will enter')

for counter in range(MAX):
    number = int(input('Enter: '))

    print("Total is ", total)
    total = total + number
    print("Total has been changed to", total)

print(f'The total is {total}')

