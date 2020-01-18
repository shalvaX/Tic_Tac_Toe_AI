from random import randrange

class Tic_Tac_Game:
    def __init__(self,p1):
        self.p1=p1
        self.table = [[],[],[],
                      [],[],[],
                      [],[],[]]

    def WinState(self,table):
        try:
            if (table[0]==table[1]==table[2] and len(table[0])>0 or table[0]==table[3]==table[6] and len(table[0])>0 or table[0]==table[4]==table[8] and len(table[0])>0 or table[1]==table[4]==table[7] and len(table[1])>0 or table[2]==table[4]==table[6] and len(table[2])>0 or table[2]==table[5]==table[8] and len(table[2])>0 or table[3]==table[4]==table[5] and len(table[3])>0 or table[6]==table[7]==table[8] and len(table[6])>0):
                return 1
            else:
                return 0
        except:
            pass

    def PlayerMove(self,p1):
        print("choices from 0 to 8;")
        c1 = input(p1 + " choose:")
        if c1.isdigit():
            if 0<=int(c1) <=8 and len(self.table[int(c1)])==0 and len(c1)>0:
                self.table[int(c1)].append("X")
            else:
                print("wrong input!")
                Tic_Tac_Game.PlayerMove(self,self.p1)
        else:
            print("wrong input!")
            Tic_Tac_Game.PlayerMove(self,self.p1)
    def AIMove(self):
        count = randrange(0,8)
        stop=0
        while stop!=1:
            count -= 1
            if len(self.table[count])==0:
                self.table[count].append("O")
                stop=1
            elif len(self.table[count])==1 and count==2 or count==5 or count==8:
                if len(self.table[count-1])==0:
                    self.table[count-1].append("O")
                    stop=1
                elif len(self.table[count-2])==0:
                    self.table[count-2].append("O")
                    stop=1
            elif len(self.table[count])==1 and count==0 or count==3 or count==6:
                if len(self.table[count+1])==0:
                    self.table[count+1].append("O")
                    stop=1
                elif len(self.table[count + 2]) == 0:
                    self.table[count+2].append("O")
                    stop=1
            if count == 0:
                break

    def main(self):
        print("Welcome to tic tac toe game. You are able to play against idiot AI.")
        win=0
        while win!=1:
            Tic_Tac_Game.PlayerMove(self,self.p1)
            print(self.table[0], self.table[1], self.table[2], "" + "\n",
                  self.table[3], self.table[4], self.table[5], "" + "\n",
                  self.table[6], self.table[7], self.table[8])
            print("AI move")
            print("-------------------")
            Tic_Tac_Game.AIMove(self)
            print(self.table[0], self.table[1], self.table[2], "" + "\n",
                  self.table[3], self.table[4], self.table[5], "" + "\n",
                  self.table[6], self.table[7], self.table[8])
            win = Tic_Tac_Game.WinState(self, self.table)

x=Tic_Tac_Game(input("choose name:"))
x.main()
