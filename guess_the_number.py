import random
target= random.randint(1,100)
attempts=0
while True:
    try:
        user_no=input("Guess Number(Between 1 to 100) or Quit:")
        if user_no=="Quit":
             break
        attempts+=1
        user_no=int(user_no)
        if user_no==target:
            print("Correct,It is",target)
            print("You Guessed it in",attempts,"Attempts")
            break
        elif user_no > target:
            print("Too High")
        elif target > user_no:
            print("Too Low")
    except ValueError:
            print("Only Number are Allowed To Enter")     
print("___Game Over___ ") 
print("Thanks To play")
               
