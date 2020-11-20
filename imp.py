# ________PROJECT 1________#
import cv2 # Importing opencv to display image
import random#importing random to work on random function
robot=0
you=0
a=cv2.imread("D:\\downloads\\s and s.jpg")#  path of the image
b=cv2.imread("D:\\downloads\\r and r.jpg")#  path of the image
c=cv2.imread("D:\\downloads\\p and p.jpg")#  path of the image
d=cv2.imread("D:\\downloads\\r and s.jpg")#  path of the image
e=cv2.imread("D:\\downloads\\p and r.jpg")#  path of the image
f=cv2.imread("D:\\downloads\\p and s.jpg")#  path of the image
print("{'ROCK','PAPER','SISSOR'} \n"
      ".......GAME......\n"
      "the game is for ['3'] points you vs computer ")
while True :#condition 0
    x = input("choose R or P or S:")
    choose = x.upper()
    c= ("R", "P", "S")
    comp = random.choice(c)
    if choose in c:
        print(str(comp), choose)
    else:
        print("choose in B/N 'R','P','S'")
        pass
    print("")# nothing to give a line gap
    if str(comp)=="R":#  condition 1
        if str(choose)=="R":#  condition 1.1
            print("tie___press[Esc]")
            print("*_*")
            cv2.imshow("goku", b)
            cv2.waitKey(0)# it works on kyboard key functions
            cv2.destroyAllWindows()
        elif str(choose)=="P":#  condition 1.2
            print("you win___press[Esc]")
            print("^_^")
            cv2.imshow("goku", e)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            you+=1
            print(" your score:",you)
        elif str(choose)=="S":#  condition 1.3
            print("comp win___press[Esc]")
            print("'_'")
            cv2.imshow("sissor and paper", d)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            robot+=1
            print("computer score:",robot)
    elif str(comp)=="P":#  condition 2
        if str(choose)=="P":#  condition 2.1
            print("tie___press[Esc]")
            print("*_*")
        elif str(choose)=="S":#  condition 2.2
            print("you win___press[Esc]")
            you+=1
            cv2.imshow("goku", f)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("your score:",you)
        elif str(choose)=="R":#  condition 2.3
            print("comp win___press[Esc]")
            print("'_'")
            cv2.imshow("goku", e)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            robot += 1
            print("computer score:", robot)
    elif str(comp)=="S":#  condition 3
        if str(choose)=="S":#  condition 3.1
            print("tie___press[Esc]")
            print("*_*")
            cv2.imshow("goku", a)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif str(choose)=="P":#  condition 3.2
            print("comp win___press[Esc]")
            print("'_'")
            cv2.imshow("goku", f)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            robot += 1
            print("computer score:", robot)
        elif str(choose)=="R":#  condition 3.3
            print("you win___press[Esc]")
            print("^_^")
            cv2.imshow("goku", d)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            you+=1
            print("your score:",you)
    if robot==3:
        print("computer won___game over")
        again = input("press y or n")
        if again.upper() == "Y":#  reseting score of computer if computer won  play again
            robot -= robot
            you -= you
            pass
        else:
            print("GOODBYE")
            break
    elif you==3:
       print("you won\//\game over/\\/")
       again = input("press y or n")
       if again.upper() == "Y":#  reseting score of player if player won  play again
           robot -= robot
           you -= you
           pass
       else:
           print("GOOD BYE")
           break
