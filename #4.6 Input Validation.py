#ask for a score
score = int(input("Enter a test score: "))

#will check if score is less than 0 each iteration
while score < 0:

    #when the score is less than 0, gives error message
    print("ERROR: the score cannot be negative. ")

    #ask for score again
    score = int(input("Enter the correct score: "))
