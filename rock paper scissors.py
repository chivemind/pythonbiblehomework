#Rock, Paper, Scissors

#Paper covers rock - (y,x)
#Scissors cut paper - (z,y)
#Rock crushes scissors -(x,z)


#Define rock, paper, scissors
x = "rock"
y = "paper"
z = "scissors"

#Define win, lose, tie
win = []
lose = []
tie = []

#Define match results
win = range{
    [y, x],
    [z, y],
    [x, z]
    }

lose = {
    [x, y],
    [y, z],
    [z, x]
    }

tie = {
    [x, x],
    [y, y],
    [z, z]
    }

#Challenge user to match
print("Hello human....")
print()
print("Your computer has challenged you to a game of Rock, Paper, Scissors...")
print()
print("Rock...")
print()
print("Paper...")
print()
print("Scissors...")
print()

while True:

    #Create match
    match = [{},{}]
    
    #Allow player to choose
    choice = input("Shoot!: ").strip().lower()
    choice = match[0]

    #Create a way for the computer to generate a random choice.
    from random import choice
    compy = (x, y, z)
    compy_choice = choice(compy) 
    compy_choice = match[1]
    
    #define potential combos
    if match in win:

        winner = "Congratulations, human...your {} has defeated the computer's feeble {}."
        output = winner.format(match[0], match[1])
        print(output)
        pass

    elif match in lose:

        loser = "Hahaha human...your inferior {} is no match for your computer's superior {}!"
        output = loser.format(match[0], match[1])
        print(output)
        pass
            
    elif match in tie:

        tie = "Does not compute...somehow you drew {} at the exact same time as your computer rendered it's {}. Try again."
        output = tie.format(match[0], match[1])
        print(output)
        pass
    
else:
    pass
  
