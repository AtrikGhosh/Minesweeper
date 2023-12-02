import random
import os
import time
class Board:
    def __init__(self,size,bombcount):
        self.size = size
        self.bombcount = bombcount

        self.board = self.newboard()
        self.dug = 0
        self.flagged = 0
        self.visited = [[-1 for i in range(self.size)] for j in range(self.size)]
        self.assignboardvalue()
    


    def newboard(self):
        board = [[None for i in range(self.size)] for j in range(self.size)]

        bombno = 0

        while(bombno<self.bombcount):
            row = random.randint(0,self.size-1)
            col = random.randint(0,self.size-1)

            if(board[row][col] != "*"):
                board[row][col] = "*"
                bombno +=1
        return board

    def assignboardvalue(self):
        for row in range(self.size):
            for column in range(self.size):
                if(self.board[row][column] != "*"):
                    surrounding_bomb_count = 0
                    for subrow in range(max(0,row-1),min(self.size,(row+1)+1)):
                        for subcol in range(max(0,column-1),min(self.size,(column+1)+1)):
                            if(self.board[subrow][subcol] == "*"):
                                surrounding_bomb_count+=1
                    self.board[row][column] = surrounding_bomb_count
    def printbomb(self):
        print("  |",end = "")
        for i in range(self.size):
            print(i,end = " ")
        print()
        for i in range(self.size+1):
            print("--",end = "")
        print("-")
        for i in range(self.size):
            print(i,end = " |")
            for j in range(self.size):
                if(self.visited[i][j] == 1 or self.board[i][j] == "*"):
                    print(self.board[i][j],end = "|")
                elif(self.visited[i][j] == 0):
                    print("X",end = "|")
                else:
                    print(" ",end = "|")
            print()


    def printboard(self):
        print("  |",end = "")
        for i in range(self.size):
            print(i,end = " ")
        print()
        for i in range(self.size+1):
            print("--",end = "")
        print("-")
        for i in range(self.size):
            print(i,end = " |")
            for j in range(self.size):
                if(self.visited[i][j] == 1):
                    print(self.board[i][j],end = "|")
                elif(self.visited[i][j] == 0):
                    print("X",end = "|")
                else:
                    print(" ",end = "|")
            print()
        


    def dig(self,row,column):
        if(self.visited[row][column] >=0):
            pass
        elif(self.board[row][column] == "*"):
            self.printbomb()
            print("GAME OVER!!")
            time.sleep(5)
            Q = input("Do you want to restart? [Y/N]: ")
            if(Q.lower() == 'y'):
                startgame()
            else:
                exit()
            
        else:
            self.visited[row][column] = 1
            self.dug +=1 
            if(self.board[row][column] == 0):
                for subrow in range(max(0,row-1),min(self.size,(row+1)+1)):
                    for subcol in range(max(0,column-1),min(self.size,(column+1)+1)):
                        if(self.visited[subrow][subcol]<=0):
                            self.dig(subrow,subcol)
            
    def flag(self,row,column):
        if(self.visited[row][column] == -1):
            self.visited[row][column] = 0
            self.flagged+=1
        
    def unflag(self,row,column):
        if(self.visited[row][column] == 0):
            self.visited[row][column] = -1
            self.flagged-=1
                            

def play(size,bombcount):
    B = Board(size,bombcount)
    while(B.dug<size**2 - bombcount):
        os.system('cls')
        B.printboard()
        action = int(input('''Select option number:
    1. DIG
    2. FLAG
    3. REMOVE FLAG
'''))
        row = int(input("Enter row: "))
        column = int(input("Enter column: "))
        if(row>=size or column>=size):
            print("Please mark correct grid co-ordinates")
            continue
        if(action == 1):
            B.dig(row,column)
        elif(action == 2):
            B.flag(row,column)
        elif(action == 3):
            B.unflag(row,column)
        else:
            print("Please select a valid option number")
    B.printboard()
    print("YOU WON!!")
    time.sleep(5)
        
    
def startgame():
    size = int(input("Enter size of the minefield: "))
    bombcount = int(input("Enter number of bombs: "))

    if(size<2 or bombcount>=size**2 or bombcount<=0):
        print("INVALID!")
        Q = input("Do you want to restart? [Y/N]: ")
        if(Q.lower() == 'y'):
            startgame()
        time.sleep(2)
         
    else:
        play(size,bombcount)
        
        
        
            
startgame()
            

'''
-1 = notvisited
0 = flag
1 = visited
'''
