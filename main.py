from tkinter import *
from tkinter import messagebox
import tkinter         

def changestate():
    buttone = tkinter.Button(sub,text = "Start Game",command=called,state = DISABLED)
    buttone.place(x = 200 , y = 200)

def called():
    changestate()
    main = Toplevel(sub)
    main.geometry("500x500") 
    main.title("Game Started")   
    global alt
    global list
    alt = False
    list = [1,4,5,6,7,8,9,10,11,12,13]
    player1 =  x23.get()
    player2 = y23.get()



    def endgame(a):
        if a == 0:
            messagebox.showinfo("Winner", "Winner is " + player1)
            buttone = tkinter.Button(sub,text = "Start Game",command=called)
            buttone.place(x = 200 , y = 200)
            main.destroy()

        if a == 1:
            messagebox.showinfo("Winner", "Winner is " + player2)    
            buttone = tkinter.Button(sub,text = "Start Game",command=called)
            buttone.place(x = 200 , y = 200)
            main.destroy()

    def endgame2():       
            messagebox.showinfo("Results", "Tie") 
            buttone = tkinter.Button(sub,text = "Start Game",command=called)
            buttone.place(x = 200 , y = 200)
            main.destroy() 

    def commando(a,b,c):
        global alt
        global list


        if (alt == False):
            textF = "   X   "
            alt = True
            l = 0
            list[c]=l

        else :
            textF = "   O   "
            alt = False
            l = 1
            list[c]=l
        
        but = tkinter.Button(main,text = textF,padx= 50,pady=50,state=DISABLED)
        but.place(x=a,y=b)
        print(list)
        
        if list[1]==list[2]==list[3]:
            endgame(list[1])
        if list[1]==list[5]==list[9]:
            endgame(list[1])
        if list[1]==list[4]==list[7]:
            
            endgame(list[1])
        if list[3]==list[5]==list[7]:
              endgame(list[3])  
        if list[4]==list[5]==list[6]:
            endgame(list[4])
        if list[7]==list[8]==list[9]:
            endgame(list[7])
        if list[2]==list[5]==list[8]:
            endgame(list[2])
        if list[3]==list[6]==list[9]:
            endgame(list[3])           

        else:
            i=0
            while i<10:
                if list[i] == 1 or list[i] == 0:
                        i=i+1
                        print(i)
                else:
                    break        
            if i == 10:
                endgame2()           
                        
                        
                        
                            
                        

                    
                    

        return alt



    a = "Click"

    playname1 = tkinter.Label(main,text="Player 1 is "+player1+" Respresenting X ")
    playname2 = tkinter.Label(main,text="Player 2 is "+player2+" Respresenting O ")

    but1 = tkinter.Button(main,text = a,padx=50,pady=50,command=lambda:commando(10,10,1))
    but2 = tkinter.Button(main,text = a,padx=50,pady=50,command=lambda:commando(10+150,10,2))
    but3 = tkinter.Button(main,text = a,padx=50,pady=50,command=lambda:commando(10+300,10,3))

    but4 = tkinter.Button(main,text = a,padx=50,pady=50,command=lambda:commando(10,10+150,4))
    but5 = tkinter.Button(main,text = a,padx=50,pady=50,command=lambda:commando(10+150,10+150,5))
    but6 = tkinter.Button(main,text = a,padx=50,pady=50,command=lambda:commando(10+300,10+150,6))

    but7 = tkinter.Button(main,text = a,padx=50,pady=50,command=lambda:commando(10,10+300,7))
    but8 = tkinter.Button(main,text = a,padx=50,pady=50,command=lambda:commando(10+150,10+300,8))
    but9 = tkinter.Button(main,text = a,padx=50,pady=50,command=lambda:commando(10+300,10+300,9))

    but1.place(x=10,y=10)
    but2.place(x=10+150,y=10)
    but3.place(x=10+300,y=10)

    but4.place(x=10,y=10+150)
    but5.place(x=10+150,y=10+150)
    but6.place(x=10+300,y=10+150)

    but7.place(x=10,y=10+300)
    but8.place(x=10+150,y=10+300)
    but9.place(x=10+300,y=10+300)

    playname1.place(x=100,y=445)
    playname2.place(x=100,y=460)

    mainloop()
    return 

sub = Tk()
sub.geometry("500x500")
sub.title("2 Player Tic Tac Toe Game")
x21 = tkinter.Label(sub,text="Enter Name of Player 1")
x22 = tkinter.Label(sub,text="Enter Name of Player 1")
x23 = tkinter.Entry(sub)
y23 = tkinter.Entry(sub)
x21.place(x = 110, y = 100)
x22.place(x = 110, y = 130)
x23.place(x = 250 , y = 100)
y23.place(x = 250 , y = 130)
    

buttone = tkinter.Button(sub,text = "Start Game",command=called)
buttone.place(x = 200 , y = 200)


mainloop()


# Ashwin Batchu Owns This
