def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("______________________")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Answer here (A, B, C, D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num +=1

    display_score(correct_guesses, guesses)

#______________________________
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("Wrong answer :(")
        return 0
#______________________________
def display_score(correct_guesses, guesses):
    print("----------------------")
    print("RESULTS")
    print("----------------------")
    print("Answers:", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Your guesses were:", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    total_score = float((correct_guesses/len(questions))*100)
    print("Your total score is {}%".format(total_score))
#______________________________
def play_again():
    response = input("Do you want to play again? (Y/N)").upper()
    if response == "YES":
        return True
    else:
        return False
#______________________________


questions = {
    "Who created Bitcoin?: ": "B",
    "Who discovered Brazil?: ": "C",
    "Where are Monty Python from?: ": "A",
    "What is the first name of the 007 agent?: ": "C"
}
options = [["A.Elon Musk", "B.Sakamoto", "C.Bill Gates"],
           ["A.Columbus", "B.Bonaparte", "C.Pedro Alvares Cabral"],
           ["A.Britain", "B.Sylicon Valley", "C.New York"],
           ["A.Bond", "B.Mr. Pink", "C.James"]]
new_game()

while play_again():
    new_game()
print("Thanks for participating!")