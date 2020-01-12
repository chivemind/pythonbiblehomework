#Collect name, age, email and date of birth
#Check if info is correct
#Allow corrections
#Create username and password
#Ask if user wants to be added to mailing list
#Allow user to be removed from mailing list
#Have a nice day

mailing_list = list()

while True:
    name = input("What's your name?: ").strip().title()

    age = int(input("How old are you?: "))

    email = input("What's your email address?: ").strip().lower()
    
    birthday = input("What's your birthday? (xx/xx/xxxx): ").strip()

    string = "Verify your information. {}, {}, {}, {}."
    output = string.format(name, age, email, birthday)
    print(output)

    tf = input("Correct:? y/n ").strip().lower()

    if tf == "y":
        username = email[:email.index("@")]
        password = birthday[-4:]

        string2 = "Okay, {}. Your username is {} and your password is {}. Thank you."
        output2 = string2.format(name, username, password)
        print(output2)

        add = input("{}, would you like to be added to our mailing list?: y/n ".format(name)).strip().lower()
        if add == "y":
            mailing_list.append(email)
            print(mailing_list)

            remove = input("To be removed, press 'R' now. ").strip().capitalize()
            if remove == "R":
                mailing_list.remove(email)
                print("Unsubscribed")
                
            else:
                print("Have a nice day.")

        else:
            print("Have a nice day.")
        
    else:
        correction = input("Which item is incorrect?: name, age, email, birthday? ").strip().lower()

        if correction == "name":
            name = input("What's your name? ").strip().title()

            string = "Verify your information. Name {}, Age {}, Email {}, Birthday {}."
            output = string.format(name, age, email, birthday)
            print(output)

            tf = input("Correct:? y/n ").strip().lower()

            if tf == "y":
                    username = email[:email.index("@")]
                    password = birthday[-4:]

                    output = string.format(name, age, email, birthday)                    
                    string2 = "Okay, {}. Your username is {} and your password is {}. Thank you."
                    output2 = string2.format(name, username, password)
                    print(output2)

                    add = input("Would you like to be added to our mailing list?: y/n ").strip().lower()
                    if add == "y":
                        mailing_list.append(email)
                        print(mailing_list)

                        remove = input("To be removed, press 'R' now. ").strip().capitalize()
                        if remove == "R":
                            mailing_list.remove(email)
                            print("Unsubscribed")
                
                        else:
                            print("Have a nice day.")

                    else:
                        print("Have a nice day.")

            else:
                pass

        elif correction == "age":
            age = int(input("How old are you?: "))
            
            string = "Verify your information. Name {}, Age {}, Email {}, Birthday {}."
            output = string.format(name, age, email, birthday)
            print(output)

            tf = input("Correct:? y/n ").strip().lower()

            if tf == "y":
                    username = email[:email.index("@")]
                    password = birthday[-4:]

                    output = string.format(name, age, email, birthday)
                    string2 = "Okay, {}. Your username is {} and your password is {}. Thank you."
                    output2 = string2.format(name, username, password)
                    print(output2)

                    add = input("{}, would you like to be added to our mailing list?: y/n ".format(name)).strip().lower()
                    if add == "y":
                        mailing_list.append(email)
                        print(mailing_list)

                        remove = input("To be removed, press 'R' now. ").strip().capitalize()
                        if remove == "R":
                            mailing_list.remove(email)
                            print("Unsubscribed")
                
                        else:
                            print("Have a nice day.")

                    else:
                        print("Have a nice day.")

            else:
                 pass

        elif correction == "email":
            email = input("What's your email address? ").strip().lower()

            string = "Verify your information. Name {}, Age {}, Email {}, Birthday {}."
            output = string.format(name, age, email, birthday)
            print(output)

            tf = input("Correct:? y/n ").strip().lower()

            if tf == "y":
                    username = email[:email.index("@")]
                    password = birthday[-4:]

                    output = string.format(name, age, email, birthday)
                    string2 = "Okay, {}. Your username is {} and your password is {}. Thank you."
                    output2 = string2.format(name, username, password)
                    print(output2)

                    add = input("{}, would you like to be added to our mailing list?: y/n ".format(name)).strip().lower()
                    if add == "y":
                        mailing_list.append(email)
                        print(mailing_list)

                        remove = input("To be removed, press 'R' now. ").strip().capitalize()
                        if remove == "R":
                            mailing_list.remove(email)
                            print("Unsubscribed")
                
                        else:
                            print("Have a nice day.")

                    else:
                        print("Have a nice day.")

            else:
                pass

        elif correction == "birthday":
            birthday = input("What is your birthday? xx/xx/xxxx ")

            string = "Verify your information. Name {}, Age {}, Email {}, Birthday {}."
            output = string.format(name, age, email, birthday)
            print(output)

            tf = input("Correct:? y/n ").strip().lower()

            if tf == "y":
                    username = email[:email.index("@")]
                    password = birthday[-4:]

                    output = string.format(name, age, email, birthday)
                    string2 = "Okay, {}. Your username is {} and your password is {}. Thank you."
                    output2 = string2.format(name, username, password)
                    print(output2)

                    add = input("{}, would you like to be added to our mailing list?: y/n ".format(name)).strip().lower()
                    if add == "y":
                        mailing_list.append(email)
                        print(mailing_list)

                        remove = input("To be removed, press 'R' now. ").strip().capitalize()
                        if remove == "R":
                            mailing_list.remove(email)
                            print("Unsubscribed")
                
                        else:
                            print("Have a nice day.")

                        
                    else:
                        print("Have a nice day.")

            else:
                pass


            



    
