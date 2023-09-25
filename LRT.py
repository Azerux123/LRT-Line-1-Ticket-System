# Dela Rosa, Carl KC & Alcanzo, John Cleo
# BSIS - NS - 2B

import csv
from tkinter import *
from tkinter import messagebox
import tkinter
import string

class LRTTicket(Frame):
    def __init__(self):
        
        Frame.__init__(self)
        self.stat = 0        
        self.stat2 = 0
        self.nameStat = ""
        self.nameStat2 = ""
        self.qtyTicket = 0
        self.price = 0 
        self.pricer = 0
        self.payment = 0
        self.receipt = 0
        self.user_int = 0
        self.balance = 0
        self.mainWin = tkinter.Tk()
        self.mainWin.title("LRT Line 1 Ticket System")
        frame = tkinter.Frame(self.mainWin)
        frame.pack()
        
        self.main_frame = tkinter.LabelFrame(frame, text ="LRT Line 1", bg= "#576CA8")
        self.main_frame.grid(row=0, column=0)
        
        self.label1 = tkinter.Label(self.main_frame, text = "Choose Option",font = ("Tahoma, 20"), fg= "white", bg="#6C87D1")
        self.label1.grid(row=0, column=1)
        
        self.sjtTicket = tkinter.Button(self.main_frame, text = "Single Journey Ticket", command = self.sjt_func, bg="#F5F3F5")
        self.sjtTicket.grid(row=1, column=0)
        
        self.cardHolder = tkinter.Button(self.main_frame, text = "Card Holder", command= self.card_holder_func, bg= "#F5F3F5")
        self.cardHolder.grid(row=1, column=2)
        
        for widget in self.main_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    def card_holder_func(self):
        self.cardWin = tkinter.Tk()
        self.cardWin.title("Card Load")
        frame = tkinter.Frame(self.cardWin)
        frame.pack()
        self.receipt = 1
        
        self.subframe1 = tkinter.LabelFrame(frame, text = "LOAD", bg="#1B264F", fg='white')
        self.subframe1.grid(row=1, column=1)
        
        self.Originlabel1 = tkinter.Label(frame, text = "TOP UP YOUR TO CARD",font = ("Tahoma, 20"),background="#6C87D1", fg="white")
        self.Originlabel1.grid(row=0, column=1)

        self.label5 = tkinter.Label(self.subframe1, text= "How much are you going to top up?", font=("Tahoma"), fg= "white", bg= "#274690")
        self.label5.grid(row= 1, column=0)

        self.load = IntVar
        self.load = tkinter.Entry(self.subframe1, font=("Tahoma"), textvariable=self.load)
        self.load.grid(row = 2, column=0)

        self.loadButton = tkinter.Button(self.subframe1, text = "Top Up", font= "tahoma", command= self.load_func)
        self.loadButton.grid(row = 2, column= 1)

        for widget in self.subframe1.winfo_children():
            widget.grid_configure(padx=10, pady=5)
    
    def load_func(self):
        self.user_int= str(self.load.get())
        data = [self.user_int]
        with open('rec.csv', 'w', newline='') as w:   
                writer = csv.writer(w)
                writer.writerow(data)

        self.cardWin.destroy()

        self.SuccessWin = tkinter.Tk()
        self.SuccessWin.title("Successfully Top Up")
        frame = tkinter.Frame(self.SuccessWin)
        frame.pack()
        
        self.subframe2 = tkinter.LabelFrame(frame, text = "YOU HAVE TOP UP SUCCESSFULLY!!!", font=("Tahoma, 20"), bg = "#274690", fg="white")
        self.subframe2.grid(row= 0, column=0)

        self.okayButton = tkinter.Button(self.subframe2, text= "Continue", font=("Tahoma"), command=self.sjt_func)
        self.okayButton.grid(row = 1, column=0, columnspan= 10)


        
    # def success(self):
    #     self.SuccessWin = tkinter.Tk()
    #     self.SuccessWin.title("Successfully Top Up")
    #     frame = tkinter.Frame(self.SuccessWin)
    #     frame.pack()
        
    #     self.subframe2 = tkinter.LabelFrame(frame, text = "YOU HAVE TOP UP SUCCESSFULLY", font="Tahoma, 20")
    #     self.subframe2.grid(row= 0, column=0)

            
    def sjt_func(self):
        self.qtyWin = tkinter.Tk()
        self.qtyWin.title("Ticket Origin / Destination ")
        frame = tkinter.Frame(self.qtyWin)
        frame.pack()
        self.mainWin.destroy()
        if self.receipt == 1:
            self.SuccessWin.destroy()
        
        self.subframe = tkinter.LabelFrame(frame, text = "Origin Station", bg= "#274690", fg= "white")
        self.subframe.grid(row=1, column=1)
        
        self.Originlabel = tkinter.Label(frame, text = "Choose your Origin",font = ("Tahoma, 20"), background="#6C87D1", fg="White")
        self.Originlabel.grid(row=0, column=1)
        
        self.spacer = tkinter.Label(frame)
        self.spacer.grid(row=0, column=3)
        
        self.Button1 = tkinter.Button(self.subframe, text = "Baclaran Station", command= self.b1)
        self.Button1.grid(row=2, column=0)       
    
        self.Button2 = tkinter.Button(self.subframe, text = "EDSA Station", command= self.b2)
        self.Button2.grid(row=2, column=1)   
        
        self.Button3 = tkinter.Button(self.subframe, text = "Libertad Station", command= self.b3)
        self.Button3.grid(row=2, column=2)
        
        self.Button4 = tkinter.Button(self.subframe, text = "Gil Puyat Station", command= self.b4)
        self.Button4.grid(row=2, column=3)
        
        self.Button5 = tkinter.Button(self.subframe, text = "Vito Cruz Station", command= self.b5)
        self.Button5.grid(row=2, column=4)
        
        self.Button6 = tkinter.Button(self.subframe, text = "Quirino Ave. Station", command= self.b6)
        self.Button6.grid(row=2, column=5)
        
        self.Button7 = tkinter.Button(self.subframe, text = "Pedro Gil Station", command= self.b7)
        self.Button7.grid(row=2, column=6)
        
        self.Button8 = tkinter.Button(self.subframe, text = "United Nations Station", command= self.b8)
        self.Button8.grid(row=2, column=7)
        
        self.Button9 = tkinter.Button(self.subframe, text = "Central Terminal Station", command= self.b9)
        self.Button9.grid(row=2, column=8)
        
        self.Button10 = tkinter.Button(self.subframe, text = "Carriedo Station", command= self.b10)
        self.Button10.grid(row=2, column=9)
        
        self.Button11 = tkinter.Button(self.subframe, text = "Doroteo Jose Station", command= self.b11)
        self.Button11.grid(row=3, column=0)
        
        self.dst12 = tkinter.Button(self.subframe, text = "Bambang Station", command= self.b12)
        self.dst12.grid(row=3, column=1)
        
        self.dst13 = tkinter.Button(self.subframe, text = "Tayuman Station", command= self.b13)
        self.dst13.grid(row=3, column=2)
        
        self.dst14 = tkinter.Button(self.subframe, text = "Blumentritt Station", command= self.b14)
        self.dst14.grid(row=3, column=3)
        
        self.dst15 = tkinter.Button(self.subframe, text = "Abad Santos Station", command= self.b15)
        self.dst15.grid(row=3, column=4)
        
        self.dst16 = tkinter.Button(self.subframe, text = "R.Papa Station", command= self.b16)
        self.dst16.grid(row=3, column=5)
        
        self.dst17 = tkinter.Button(self.subframe, text = "5th Avenue Station", command= self.b17)
        self.dst17.grid(row=3, column=6)
        
        self.dst18 = tkinter.Button(self.subframe, text = "Monumento Station", command= self.b18)
        self.dst18.grid(row=3, column=7)
        
        self.dst19 = tkinter.Button(self.subframe, text = "Balintawak Station", command= self.b19)
        self.dst19.grid(row=3, column=8)
        
        self.dst20 = tkinter.Button(self.subframe, text = "Roosevelt Station", command= self.b20)
        self.dst20.grid(row=3, column=9)
        
        
        for widget in self.subframe.winfo_children():
            widget.grid_configure(padx=10, pady=5)
            
    def b1(self):
        self.stat = 1
        self.destination()
        self.nameStat = "Baclaran Station"
        self.qtyWin.destroy()
        
    def b2(self):
        self.stat = 2
        self.nameStat = "EDSA Station"
        self.destination()
        self.qtyWin.destroy()
        
    def b3(self):
        self.stat = 3
        self.nameStat = "Libertad Station"
        self.destination()
        self.qtyWin.destroy()
    
    def b4(self):
        self.stat = 4
        self.nameStat = "Gil Puyat Station"
        self.destination()
        self.qtyWin.destroy()
        
    def b5(self):
        self.stat = 5
        self.nameStat = "Vito Cruz Station"
        self.destination()
        self.qtyWin.destroy()
        
    def b6(self):
        self.stat = 6
        self.nameStat = "Quirino Ave. Station"
        self.destination()
        self.qtyWin.destroy()
        
    def b7(self):
        self.stat = 7
        self.nameStat = "Pedro Gil Station"
        self.destination()
        self.qtyWin.destroy()

    def b8(self):
        self.stat = 8
        self.nameStat = "United Nations Station"
        self.destination()
        self.qtyWin.destroy()
    
    def b9(self):
        self.stat = 9
        self.nameStat = "Central Terminal Station"
        self.destination()
        self.qtyWin.destroy()
    
    def b10(self):
        self.stat = 10
        self.nameStat = "Carriedo Station"
        self.destination()
        self.qtyWin.destroy()
    
    def b11(self):
        self.stat = 11
        self.nameStat = "Doroteo Jose Station"
        self.destination()
        self.qtyWin.destroy()
    
    def b12(self):
        self.stat = 12
        self.nameStat = "Bambang Station"
        self.destination()
        self.qtyWin.destroy()
    
    def b13(self):
        self.stat = 13
        self.nameStat = "Tayuman Station"
        self.destination()
        self.qtyWin.destroy()
        
    def b14(self):
        self.stat = 14
        self.nameStat = "Blumentrit Station"
        self.destination()
        self.qtyWin.destroy()
        
    def b15(self):
        self.stat = 15
        self.nameStat = "Abad Santos Station"
        self.destination()
        self.qtyWin.destroy()
    
    def b16(self):
        self.stat = 16
        self.nameStat = "Roosevelt Station"
        self.destination()
        self.qtyWin.destroy()
    
    def b17(self):
        self.stat = 17
        self.nameStat = "Roosevelt Station"
        self.destination()
        self.qtyWin.destroy()
    
    def b18(self):
        self.stat = 18
        self.nameStat = "Roosevelt Station"
        self.destination()
        self.qtyWin.destroy()
        
    def b19(self):
        self.stat = 19
        self.nameStat = "Roosevelt Station"
        self.destination()
        self.qtyWin.destroy()
        
    def b20(self):
        self.stat = 20
        self.nameStat = "Roosevelt Station"
        self.destination()
        self.qtyWin.destroy()
            
    def destination(self):
        self.dstWin = tkinter.Tk()
        self.dstWin.title("Ticket Destination ")
        frame = tkinter.Frame(self.dstWin)
        frame.pack()
        
        self.DestinationLabel = tkinter.Label(frame, text = "Choose your Destination",font = ("Tahoma, 20"), bg= "#6C87D1", fg="white")
        self.DestinationLabel.grid(row=0, column=1)
        
        self.dstSubbrame = tkinter.LabelFrame(frame, text="Origin Station", bg= "#274690", fg="white")
        self.dstSubbrame.grid(row=1, column=1)
        
        self.dst1 = tkinter.Button(self.dstSubbrame, text = "Baclaran Station", command= self.d1)
        self.dst1.grid(row=2, column=0)       
    
        self.dst2 = tkinter.Button(self.dstSubbrame, text = "EDSA Station", command= self.d2)
        self.dst2.grid(row=2, column=1)   
        
        self.dst3 = tkinter.Button(self.dstSubbrame, text = "Libertad Station", command= self.d3)
        self.dst3.grid(row=2, column=2)
        
        self.dst4 = tkinter.Button(self.dstSubbrame, text = "Gil Puyat Station", command= self.d4)
        self.dst4.grid(row=2, column=3)
        
        self.dst5 = tkinter.Button(self.dstSubbrame, text = "Vito Cruz Station", command= self.d5)
        self.dst5.grid(row=2, column=4)
        
        self.dst6 = tkinter.Button(self.dstSubbrame, text = "Quirino Ave. Station", command= self.d6)
        self.dst6.grid(row=2, column=5)
        
        self.dst7 = tkinter.Button(self.dstSubbrame, text = "Pedro Gil Station", command= self.d7)
        self.dst7.grid(row=2, column=6)
        
        self.dst8 = tkinter.Button(self.dstSubbrame, text = "United Nations Station", command= self.d8)
        self.dst8.grid(row=2, column=7)
        
        self.dst9 = tkinter.Button(self.dstSubbrame, text = "Central Terminal Station", command= self.d9)
        self.dst9.grid(row=2, column=8)
        
        self.dst10 = tkinter.Button(self.dstSubbrame, text = "Carriedo Station", command= self.d10)
        self.dst10.grid(row=2, column=9)
        
        self.dst11 = tkinter.Button(self.dstSubbrame, text = "Doroteo Jose Station", command= self.d11)
        self.dst11.grid(row=3, column=0)
        
        self.dst12 = tkinter.Button(self.dstSubbrame, text = "Bambang Station", command= self.d12)
        self.dst12.grid(row=3, column=1)
        
        self.dst13 = tkinter.Button(self.dstSubbrame, text = "Tayuman Station", command= self.d13)
        self.dst13.grid(row=3, column=2)
        
        self.dst14 = tkinter.Button(self.dstSubbrame, text = "Blumentritt Station", command= self.d14)
        self.dst14.grid(row=3, column=3)
        
        self.dst15 = tkinter.Button(self.dstSubbrame, text = "Abad Santos Station", command= self.d15)
        self.dst15.grid(row=3, column=4)
        
        self.dst16 = tkinter.Button(self.dstSubbrame, text = "R.Papa Station", command= self.d16)
        self.dst16.grid(row=3, column=5)
        
        self.dst17 = tkinter.Button(self.dstSubbrame, text = "5th Avenue Station", command= self.d17)
        self.dst17.grid(row=3, column=6)
        
        self.dst18 = tkinter.Button(self.dstSubbrame, text = "Monumento Station", command= self.d18)
        self.dst18.grid(row=3, column=7)
        
        self.dst19 = tkinter.Button(self.dstSubbrame, text = "Balintawak Station", command= self.d19)
        self.dst19.grid(row=3, column=8)
        
        self.dst20 = tkinter.Button(self.dstSubbrame, text = "Roosevelt Station", command= self.d20)
        self.dst20.grid(row=3, column=9)    
            
        for widget in self.dstSubbrame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
            
    def d1(self):
        self.stat2 = 1
        self.nameStat2 = "Baclaran Station"
        self.solve()
        self.dstWin.destroy()
        
    def d2(self):
        self.stat2 = 2
        self.nameStat2 = "EDSA Station"
        self.solve()
        self.dstWin.destroy()
     
    def d3(self):
        self.stat2 = 3
        self.nameStat2 = "Libertad Station"
        self.solve()
        self.dstWin.destroy()
        
    def d4(self):
        self.stat2 = 4
        self.nameStat2 = "Gil Puyat Station"
        self.solve()
        self.dstWin.destroy()
        
    def d5(self):
        self.stat2 = 5
        self.nameStat2 = "Vito Cruz Station"
        self.solve()
        self.dstWin.destroy()
        
    def d6(self):
        self.stat2 = 6
        self.nameStat2 = "Quirino Ave. Station"
        self.solve()    
        self.dstWin.destroy()
      
    def d7(self):
        self.stat2 = 7
        self.nameStat2 = "Pedro Gil Station"
        self.solve()
        self.dstWin.destroy()
    
    def d8(self):
        self.stat2 = 8
        self.nameStat2 = "United Nations Station"
        self.solve()
        self.dstWin.destroy()
        
    def d9(self):
        self.stat2 = 9
        self.nameStat2 = "Central Terminal Station"
        self.solve()
        self.dstWin.destroy()
        
    def d10(self):
        self.stat2 = 10
        self.nameStat2 = "Carriedo Station"
        self.solve()
        self.dstWin.destroy()
        
    def d11(self):
        self.stat2 = 11
        self.nameStat2 = "Doroteo Jose Station"
        self.solve()
        self.dstWin.destroy()
        
    def d12(self):
        self.stat2 = 12
        self.nameStat2 = "Bambang Station"
        self.solve()    
        self.dstWin.destroy()
    
    def d13(self):
        self.stat2 = 13
        self.nameStat2 = "Tayuman Station"
        self.solve()
        self.dstWin.destroy()
        
    def d14(self):
        self.stat2 = 14
        self.nameStat2 = "Blumentrit Station"
        self.solve()
        self.dstWin.destroy()
        
    def d15(self):
        self.stat2 = 15
        self.nameStat2 = "Abad Santos Station"
        self.solve()
        self.dstWin.destroy()
        
    def d16(self):
        self.stat2 = 16
        self.nameStat2 = "Roosevelt Station"
        self.solve()
        self.dstWin.destroy()
    
    def d17(self):
        self.stat2 = 17
        self.nameStat2 = "Roosevelt Station"
        self.solve()
        self.dstWin.destroy()
        
    def d18(self):
        self.stat2 = 18
        self.nameStat2 = "Roosevelt Station"
        self.solve()
        self.dstWin.destroy()
        
    def d19(self):
        self.stat2 = 19
        self.nameStat2 = "Roosevelt Station"
        self.solve()
        self.dstWin.destroy()
    
    def d20(self):
        self.stat2 = 20
        self.nameStat2 = "Roosevelt Station"
        self.solve()
        self.dstWin.destroy()
        
    def solve(self):
        self.ssWin = tkinter.Tk()
        self.ssWin.title("Ticket Destination ")
        frame = tkinter.Frame(self.ssWin)
        frame.pack()

        self.DestinationLabel = tkinter.Label(frame, text = "Choose ticket quantity",font = ("Tahoma, 20"), bg= "#6C87D1", fg="white")
        self.DestinationLabel.grid(row=0, column=1)
        
        self.qtySubframe = tkinter.LabelFrame(frame, text="Quantity", bg="#274690", fg="white")
        self.qtySubframe.grid(row=1, column=1)
        
        self.qty1 = tkinter.Button(self.qtySubframe, text = "1", command= self.q1)
        self.qty1.grid(row=2, column=0)       
    
        self.qty2 = tkinter.Button(self.qtySubframe, text = "2", command= self.q2)
        self.qty2.grid(row=2, column=1)   
        
        self.qty3 = tkinter.Button(self.qtySubframe, text = "3", command= self.q3)
        self.qty3.grid(row=2, column=2)
        
        self.qty4 = tkinter.Button(self.qtySubframe, text = "4", command= self.q4)
        self.qty4.grid(row=2, column=3)
        
        self.qty5 = tkinter.Button(self.qtySubframe, text = "5", command= self.q5)
        self.qty5.grid(row=2, column=4)
        
        for widget in self.qtySubframe.winfo_children():
            widget.grid_configure(padx=10, pady=5)
            
    def q1(self):
        self.qtyTicket = 1
        self.solver()
        self.ssWin.destroy()
    
    def q2(self):
        self.qtyTicket = 2
        self.solver()
        self.ssWin.destroy()
        
    def q3(self):
        self.qtyTicket = 3
        self.solver()
        self.ssWin.destroy()
        
    def q4(self):
        self.qtyTicket = 4
        self.solver()
        self.ssWin.destroy()
        
    def q5(self):
        self.qtyTicket = 5
        self.solver()
        self.ssWin.destroy()
        

    def solver(self):
        self.pricer = 0
        if self.stat2 > self.stat:
            self.pricer = self.stat2 - self.stat
        else:
            self.pricer = self.stat - self.stat2
              
        if self.pricer <= 5:
            self.price = 15
          
        elif self.pricer <= 11:
            self.price = 20

        else:
            self.price = 30 
        
        
        self.payment = self.price * self.qtyTicket
        self.main_receiptDisp()

    def main_receiptDisp(self):
        if self.receipt == 1:
            self.CardReceiptDisplay()
        else:
            self.ReceiptDisplay()

    def ReceiptDisplay(self):
        self.dispWin = tkinter.Tk()
        self.dispWin.title("Receipt ")
        frame = tkinter.Frame(self.dispWin)
        frame.pack()

        self.DestinationLabel = tkinter.Label(frame, text = "Receipt",font = ("Tahoma, 20"),bg="#6C87D1",fg="white")
        self.DestinationLabel.grid(row=0, column=1)

        self.dispFrame = tkinter.LabelFrame(frame, text="Receipt", bg="#274690", fg = "white")
        self.dispFrame.grid(row=1, column=1)
        
        self.ticketLabel1 = tkinter.Label(self.dispFrame, text="Origin: "+self.nameStat, fg = "white", bg="#274690")
        self.ticketLabel1.grid(row=1, column=2)
        
        self.ticketLabel2 = tkinter.Label(self.dispFrame, text="Destination: "+self.nameStat2, fg = "white", bg="#274690")        
        self.ticketLabel2.grid(row=2, column=2) 

        self.ticketLabel3 = tkinter.Label(self.dispFrame, text=(f"Quantity: {self.qtyTicket}"), fg = "white", bg="#274690")
        self.ticketLabel3.grid(row=3, column=2)
        
        self.ticketLabel4 = tkinter.Label(self.dispFrame, text=(f"Price: {self.payment}"), fg = "white", bg="#274690")
        self.ticketLabel4.grid(row=4, column=2)
        

    def read_rec(self):                                 
        with open("rec.csv", 'r') as file:          
            csvreader = csv.reader(file, delimiter=',')
            for row in csvreader:
                print(row)
            
        
    def CardReceiptDisplay(self):
        self.dispWin = tkinter.Tk()
        self.dispWin.title("Receipt ")
        frame = tkinter.Frame(self.dispWin)
        frame.pack()

        self.DestinationLabel = tkinter.Label(frame, text = "Receipt",font = ("Tahoma, 20"), fg = "white", bg="#6C87D1")
        self.DestinationLabel.grid(row=0, column=1)

        self.dispFrame = tkinter.LabelFrame(frame, text="Receipt", fg = "white", bg="#274690")
        self.dispFrame.grid(row=1, column=1)
        
        self.ticketLabel1 = tkinter.Label(self.dispFrame, text="Origin: "+self.nameStat, fg = "white", bg="#274690")
        self.ticketLabel1.grid(row=1, column=2)
        
        self.ticketLabel2 = tkinter.Label(self.dispFrame, text="Destination: "+self.nameStat2, fg = "white", bg="#274690")
        self.ticketLabel2.grid(row=2, column=2) 
        
        self.ticketLabel3 = tkinter.Label(self.dispFrame, text=(f"Quantity: {self.qtyTicket}"), fg = "white", bg="#274690")
        self.ticketLabel3.grid(row=3, column=2)
        
        self.ticketLabel4 = tkinter.Label(self.dispFrame, text=(f"Price: {self.payment}"), fg = "white", bg="#274690")
        self.ticketLabel4.grid(row=4, column=2)

        self.read_rec()
        self.user_int = int(self.user_int) 
        self.balance = self.user_int - self.payment
        
        self.ticketLabel5 = tkinter.Label(self.dispFrame, text=(f"Balance: {self.balance} "), fg = "white", bg="#274690")
        self.ticketLabel5.grid(row=5, column=2)

        self.updateLoad_func()

    def updateLoad_func(self):
        data = [self.balance]
        with open('rec.csv', 'w', newline='') as w:   
                writer = csv.writer(w)
                writer.writerow(data)
def main():
    LRTTicket().mainloop()

main()