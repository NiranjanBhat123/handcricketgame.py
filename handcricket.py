#hand cricket code
import random
score = 0

command=int(input("enter 0 to start \n"))

while(command!= random.randint(1,6)):{
    command:=int(input("enter a number between 1 to 6\n")),




    score:=score+command,

    print("good job!\n keep playing"),
    print("current score is ",score),
}


print("\noh! you are out !")
print("\nyour final score is,",score)
with open("highscore.txt","r") as f:
    highscore = int(f.read())
    if(score>highscore):
        print("you have broken your record!\n")
        with open("highscore.txt","w") as f:
         f.write(str(score))
