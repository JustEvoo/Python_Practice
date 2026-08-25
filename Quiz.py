
questions = ("Why is that? ",
             "Who did that? ")
options = (("A. idk", "B. who knows", "C. alr bro", "D. yes"),
           ("A. why", "B. idk bro", "C. sweet", "D. awesome"))

answers = ("C", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("="*50)
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Please enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
    question_num += 1

print("="*50)
print("RESULT")
print("="*50)

print("Guesses: ", end = "")
for guess in guesses:
    print(guess, end=" ")
print()
print("Answers: ", end = "")
for answer in answers:
    print(answer, end=" ")
print()
result = int(score / len(questions) *100)
print(f"score : {result}%")