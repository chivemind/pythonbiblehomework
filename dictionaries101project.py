films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("What film would you like to see?: ").strip().title()
    if choice in films:
         
         #Check age
         age = int(input("How old are you?: ").strip())
         
         if age >= films[choice][0]:
             
             #Check number of seats
             num_seats = films[choice][1]
             num_tix = int(input("How many tickets would you like?: ").strip())
             
             if num_seats >0 and num_tix <= num_seats:
                 print("Enjoy the film!")
                 films[choice][1] = films[choice][1]-num_tix
             else:
                 print("Sorry, we are sold out!")
         
         else:
             print("You're too young!")
    else:
        print("We don't have that film.")
            
    
