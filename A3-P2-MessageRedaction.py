#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:    W0239497 
#Student Name:  Chauntel Smith


    # YOUR CODE STARTS HERE, each line must be indented (one tab)
#Have the user input a phrase to be redacted 
#Have user input a list of letters to redact

#The Redaction
def redactLetters(userPhrase,lettersToRedact):      #I am 100% feeling better about functions now
    redactedPhrase = ""
    letterNum = 0
    #looping through the phrase to see if any of the listed letters are there 
    for letter in userPhrase:
        if letter.lower() in lettersToRedact:
            redactedPhrase += "_"   #Counting the amount of "_"
            letterNum += 1  
        else:
            redactedPhrase += letter
    return redactedPhrase, letterNum

#Main program
def main():
    #Welcome message
    print("Welcome t the Message Redaction Program!\n")
    #Loop to continue the program until the user is done
    while True: #Have user enter a phrase 
        userPhrase = input("Enter a phrase to redact (or type 'quit' to exit): ")
        if userPhrase.lower() == 'quit':    #I got stuck on this loop because I had "quit" instead of 'quit'
            break       #Have user input a list of letters to be redacted 
        #storing the list
        lettersToRedact = input("\nEnter a comma-separated list of letters to redact: ").split(',') #Took a hot minute to figure out the .split() and .strip()
        lettersToRedact =[letter.strip().lower() for letter in lettersToRedact]
        redactedPhrase, letterNum = redactLetters(userPhrase, lettersToRedact)

        #The Output of the redacted phrase with the count of letters redacted 
        print(f"Number of letters redacted: {letterNum}")
        print(f"Redacted phrase: {redactedPhrase}\n")
main()
    # YOUR CODE ENDS HERE
