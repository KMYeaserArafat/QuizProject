# Questions & answers banks,
questions = ["Question 1: What is the full meaning of CPU ?","Question 2: Freedom war of Bangladesh ? ","Question 3: Sum of 10+10 = ?"]
answers = ["control processing unit","1971","20"]
cheaker = ["Corrent", "Wrong"]



#MainOption:
def MainOption():
    print("----------------------------")
    print("1) Add new Question & Answer")
    print("2) Start Quiz")
    print("3) Exit")
    print("----------------------------")

#Update Questions 7 answer,

def Update():

    while True:
        condition1 = input("Are you want to update this question list ? (y/n) : ")
        if (condition1.lower() == "y"):
            inputNewQuestion = input("Write the Question : ")
            newQuestionList = questions.append(inputNewQuestion)
            inputNewAnswer = input("Write the  Answer : ")
            newAnswerList = answers.append(inputNewAnswer.lower())
            print("Data Updated")
            return newQuestionList
            return newAnswerList
        else:
            print("Okey, Thanks !")
            break

def Solution():
    Score = 0
    questions == questions
    answers == answers

    for x in range(len(questions)):
        print(questions[x])
        answer = input("Answer : ")
        if(answer.lower()==answers[x]):
            print(cheaker[0])
            Score+=1
        else:
            print(cheaker[1])

    print(f"Your total Question : {len(questions)} ")
    print(f"Your Score is : {Score} / {len(questions)}")
