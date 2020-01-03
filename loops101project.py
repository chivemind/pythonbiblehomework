from random import choice

while True:
    questions = [
        "Where do babies come from? ",
        "Is Santa real? ",
        "Can we go to McDonald's "
        ]
    
    question = choice(questions)
    answer = input(question).strip().lower()

    while answer != "just because":
        answer = input("...but, why? ").strip().lower()
    
