import time
def ask_question(questions ,correct_answer):

    user_answer=input(questions + "\n Your answer: ")
    if user_answer.strip( ).lower() == correct_answer.strip( ).lower():
        return True
    return False
#setup
total=5
score=0

print("welcome to quiz")
input("press Enter to start quiz")

start_time=time.time()
if ask_question("1.What data type is used to store text in Python? ", "str"):
    print("correct")
    score += 1
else:
    print("Wrong Ans , the correct Ans is: 'str'")

if ask_question("2.What will be the output of type(5.0)? ","float"):
    print("Correct ")
    score += 1
else:
    print("Wrong Ans,the correct Ans is: 'float'")

if ask_question("3.What is the correct way to declare a variable with value 10? ","x=10"):
    print("correct")
    score +=1
else:
     print("Wrong Ans , the correct Ans is: 'x = 10'")

if ask_question("4.What function is used to take input from the user in Python? ","input"):
    print("correct")
    score +=1
else:
     print("Wrong Ans , the correct Ans is: 'input'")
    
if ask_question("5.what is the output of while false ", "No output"):
    print("correct")
    score +=1
else:
     print("Wrong Ans , the correct Ans is: 'No output'")
    
end_time = time.time()
time_taken = round(end_time - start_time, 2)

print(f"\n your score is {score} out of total {total}, total time taken is {time_taken}")

if score >= 4:
    print("🚀 Great job! You’re getting Python-ready!")
else:
    print("📚 Keep practicing, you'll get there!")
 
