#rock paper scissor game between a computer and a player    
import random
def game(c,u):
    print("The computer chose:")
    if(c==1):
        print("Scissor")
    if(c==2):
        print("Rock")
    if(c==3):
        print("Paper")
    if(c==4):
        print("Lizard")
    if(c==5):
        print("Spock")        
    if(c==1):
        if(u=="r" or u=="x"):
            return("You won!")
        if(u=="p" or u=="l"):
            return("Computer won!")    
        if(u=="s"):
            return("It's a draw")
    if(c==2):
        if(u=="p" or u=="x"):
            return("You won!")
        if(u=="s" or u=="l"):
            return("Computer won!")    
        if(u=="r"):
            return("It's a draw") 
    if(c==3):
        if(u=="s" or u=="l"):
            return("You won!")
        if(u=="r" or u=="x"):
            return("Computer won!")    
        if(u=="p"):
            return("It's a draw")  
    if(c==4):
        if(u=="r" or u=="s"):
            return("You won!")
        if(u=="p" or u=="x"):
            return("Computer won!")    
        if(u=="l"):
            return("It's a draw")          
    if(c==5):
        if(u=="p" or u=="l"):
            return("You won!")
        if(u=="r" or u=="s"):
            return("Computer won!")    
        if(u=="x"):
            return("It's a draw")
count=0                                 
for i in range(1,6):            
    print(f"Round {i}")                                          
    print("Choose 'r' for rock,'p' for paper,'s' for scissor,'l' for lizard and 'x' for spock:")
    u=input("Enter the input for player:")
    c=random.randint(1,5)        
    g=game(c,u) 
    if((c==1 and (u=="r" or u=="x")) or (c==2 and (u=="p" or u=="x")) or (c==3 and (u=="s" or u=="l")) or (c==4 and (u=="r" or u=="s")) or (c==5 and (u=="p" or u=="l"))):
            count=count+1                      
    print(g)  
    print("Your score:",count)