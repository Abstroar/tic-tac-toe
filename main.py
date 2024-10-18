import math

def checker(x,user):
    count, dig, dig2 = 0, 0, 0
    for i in range(0, 3):
        c, v = 0, 0
        for j in range(0, 3):
            if i == j and x[i][j] == user:
                dig += 1
                if i == 1:
                    dig2 += 1
            if (i == 2 and j == 0 and x[i][j] == user) or ( j == 2 and i == 0 and x[i][j] == user):
                dig2 += 1

            if x[i][j] == user:
                c += 1
            if x[j][i] == user:
                v += 1
        cv = max(c,v)
        count = max(count, cv)
        if count == 3 or dig == 3 or dig2==3:
            print("win",user)
            return True
    return False

def displayx(x):
    for i in range(0,9):
        if i>0 and i%3 == 0:
            print("")
            for j in range(1,4):
                if j==2 or j==3:
                    print("|", end="")
                print("_",end="")
            print("")
        elif i !=0:
            print("|",end="")
        print(x[math.floor(i/3)][i%3],end="")



def game_start(start_table):
    displayx(start_table)
    start = 0
    end = 9
    while start<end:
        if start%2 == 0:

            x = int(input("\nPlayer1 playing with x select a location:"))
            while start_table[int(x/3)][x%3]=="x" or start_table[int(x/3)][x%3]=="o":
                print("The location is already occupied . Chose another location")
                x = int(input("\nPlayer1 playing with x select a location:"))
            # print("",int(x/3),x%3)
            start_table[int(x/3)][x%3]="x"
            x = checker(start_table,"x")
            if x == True:
                print("x player 1 is the winner")
                return
        else:
            o = int(input("\nPlayer1 playing with x select a location:"))
            while start_table[int(x/3)][x%3]=="x" or start_table[int(x/3)][x%3]=="o":
                print("The location is already occupied . Chose another location")
                x = int(input("\nPlayer1 playing with x select a location:"))
            start_table[int(o/3)][o % 3] = "o"
            o = checker(start_table,"o")
            if o:
                print("player 2 playing o is the winner")
                return
        start += 1
        displayx(start_table)
    return start_table
start = [["0","1","2"],
     ["3","4","5"],
     ["6","7","8"]]
game_start(start)