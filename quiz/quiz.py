# Call libraries and add questions and answers lists -----------------------------
f = open("questions.txt", "r")
questions = f.readlines()
f.close()

f = open("answers.txt", "r")
answers = f.readlines()
f.close()

# Functions -------------------------------------------
def askQuestions():
    score = 0
    for idx, question in enumerate(questions):
        idxOfQuestion = idx
        
        
        print(question)
        y = input("")+"\n"
        
        if y == answers[idxOfQuestion]:
            print("\r"+"Answer is Correct"+"\n")
            score = score + 1
            
        
        else:
            print("\r"+"Answer is Wrong"+"\n")
    
    print("**************** YOUR SCORE IS "+str(score))
    
def give_new_question():
    newQuestion = input("Enter a question:...")
    f = open("questions.txt", "a")
    f.write(newQuestion + "\n")
    f.close()

def give_new_answer():
    newAnswer = input("Enter the Answer:...")
    f = open("answers.txt", "a")
    f.write(newAnswer + "\n")
    f.close()

# Start of the game -----------------------------------
print("1. Ask Questions")
print("2. Add Question")
print("3. Exit Game")

choice = input("What would you like to do? 1/2/3 ")

if choice == "1":
    print("Here is a question"+"\n")
    askQuestions()
elif choice == "2":
    print("Enter a question")
    give_new_question()
    give_new_answer()
elif choice == "3":
    print("Thanks for Playing")
else:
    print("Please select number either 1, 2 or 3")



    


