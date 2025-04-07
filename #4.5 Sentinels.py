#constant variable
TAX_FACTOR = .0065

#give user instructions
print("Enter the property lot number or enter 0 to end")

#ask for initial lot number
lot = int(input('Lot number: '))

#each iteration, it checks if lot is a number aside from 0. 
while lot != 0:

    #gets the value from user
    value = float(input("Enter the property value: "))

    #calculates tax
    tax = value * TAX_FACTOR

    #print tax and ask for next lot number
    print(f'Property tax: ${tax:,.2f}')

    print("Enter the next lot number or enter 0 to end.")

    #change value of lot number
    lot = int(input('Lot number: '))

    #print("---THE LOT VALUE IS: ", lot, "---")
