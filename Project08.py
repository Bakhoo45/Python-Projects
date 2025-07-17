#include Python Quiz Game

questions = ("How many continents are there?",
             "What is the capital of India?",
             "What is the largest ocean on Earth?",
             "What is the smallest country in the world?",
             "What is the longest river in the world?")
options = (("5","6","7","8"),
           ("Delhi","Mumbai","Kolkata","Chennai"),
           ("Atlantic Ocean","Indian Ocean","Arctic Ocean","Pacific Ocean"),
           ("Vatican City","Monaco","Nauru","Tuvalu"),
           ("Amazon River","Nile River","Yangtze River","Mississippi River")
           )
answers = ("7", "Delhi", "Pacific Ocean", "Vatican City", "Nile River")
guesses= []
score = 0
question_number = 0

for question in questions:
    print("-----------------------------------")
    print("Question " + str(question_number + 1) + ": " + question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter your answer: ").lower()
    guesses.append(guess)
    
    if guess == answers[question_number].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect! The correct answer is: " + answers[question_number])
    
    question_number += 1

print("-------------RESULTS------------------")
print("Your guesses are: ", end =" ")
for guess in guesses:
    print(guess, end =" ")
print("------------------------------------")
print("Your answers are: ", end =" ")
for answer in answers:
    print(answer, end =" ") 

print("------------------------------------")
print("Your score is: " + str(score) + " out of " + str(len(questions)))
if score == len(questions): 
    print("Congratulations! You got a perfect score!")
