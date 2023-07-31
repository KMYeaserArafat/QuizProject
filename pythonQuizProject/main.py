"""
Plan :
Python Quiz :
---------------
"""
import qn_Demo as Data


while True:
    Data.MainOption()
    chooseMainOption = int(input("Enter the Option : "))

    if chooseMainOption == 1:
        print("MainOption/Add new Question & Answer")
        Data.Update()
    elif chooseMainOption == 2:
        print("MainOption/Start Quiz")
        Data.Solution()
    elif chooseMainOption==3:
        print("The Programe is closed !!")
        break

