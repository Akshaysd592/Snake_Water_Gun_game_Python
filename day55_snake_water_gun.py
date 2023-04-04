import random
player1 =0
Computer = 0 
round = 5
noproblem = int(1)
mapping = { 0:"Snake" , 1:"Water" ,2 :"Gun" }

print("------------------------------Snake Game ----------------------------------")

while(round!= 0):

  a =int(input(" player 1's turn : \n Enter your choice \n 0 For Snake\n 1 For Water \n 2 For Gun : \n "))
  if(a<0 or a>2 ):
  
    if(round==5):
      print("you entered wrong input value you should enter only 0 , 1 or 2 \n ") 
      noproblem=0
    else:
      noproblem+=1
    break
   
  b = random.randint(0,2)
  
  if((a==0 and b==0) or (a==1 and b==1) or(a==2 and b==2)):
        print(f"Player 1 selected  ==> {mapping[a]} \nComputer selected ==> {mapping[b]}\n")
        print("Match Draw\n")
  elif(a==0 and b==1 ) or (a==1 and b== 2) or (a==2 and b==0):
       print(f"Player 1 selected  ==> {mapping[a]} \nComputer selected  ==> {mapping[b]}\n")
       print("player 1 wins\n")
       player1+=1
  else:
       print(f"Player 1 selected  ==> {mapping[a]} \nComputer selected ==>  {mapping[b]}\n")
       print("Computer wins\n ")
       Computer+=1

  print(f"Player 1 score is {player1}  ")
  print(f"Computer score is {Computer} \n ")
 
  round -= 1
  print(f"--------------------Round left is {round}------------------------------- \n")
  if(round>0):
   print(" If you want to exit enter any value other than 0, 1 , 2 :\n ")
  if(round==0):
    print("Round finished\n -------------------- Game Over  --------------------\n")


if(noproblem !=0 ):
    print("\n\n")
    print(f"Player 1 score is {player1} \n ")
    print(f"Computer score is {Computer} \n ")
    if(player1>Computer):
       print("Player1 wins the match\n\n ")

    elif(player1<Computer):
       print("Computer win the match \n\n")
    elif(player1 == Computer):
       print("Match Draw No-one wins the match\n\n")













