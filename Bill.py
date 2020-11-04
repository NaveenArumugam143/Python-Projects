import tkinter as tk
from tkinter import *
import datetime
class Customer:
    def __init__(self,window):
        self.window=window
        self.window.title("Billing Software")
        window.geometry("1388x1400+0+0")
        window.config(background="lightgreen")
        frame=tk.Frame(window)
        frame.grid()
        
        frame_title=Frame(frame,width=1370,height=50,bg="lightblue",bd=14,padx=10,relief=RIDGE)
        frame_title.grid(row=0,column=0,columnspan=4,sticky="W")

        frame_1=Frame(frame,width=1300,height=100,bg="green",padx=10,relief=RIDGE)
        frame_1.grid(row=1,column=0,columnspan=4,sticky="W")

        frame_21=Frame(frame,width=1370,height=500,bg="white",bd=14,padx=150,relief=RIDGE,pady=15)
        frame_21.grid(row=2,column=0,columnspan=10,sticky="W")

        # frame_21=Frame(frame,width=1000,height=480,bg="white",bd=14,padx=100,relief=RIDGE)
        # frame_21.grid(row=2,column=0,columnspan=8,sticky="W")

        lable_3=Label(frame_21,text="Material Name",pady=5,padx=20,bg="white",height=2)
        lable_3.grid(row=0,column=0)
        lable_4=Label(frame_21,text="Quantity",pady=5,padx=20,bg="white",height=2)
        lable_4.grid(row=2,column=0,columnspan=4)
        lable_5=Label(frame_21,text="Price",pady=5,padx=20,bg="white",height=2)
        lable_5.grid(row=4,column=0)
        lable_6=Label(frame_21,text="Discount",pady=5,padx=20,bg="white",height=2)
        lable_6.grid(row=6,column=0)
        lable_7=Label(frame_21,text="Total Amount",pady=5,padx=20,bg="white",height=2)
        lable_7.grid(row=8,column=0)
        
        lable_8=Label(frame_21,text="Date & Time",pady=5,padx=20,bg="white",height=2)
        lable_8.grid(row=10,column=0)
        lable_9=Label(frame_21,text="Buyer Name",pady=5,padx=20,bg="white",height=2)
        lable_9.grid(row=12,column=0)
        lable_10=Label(frame_21,text="Phone Number",pady=5,padx=20,bg="white",height=2)
        lable_10.grid(row=14,column=0)
        lable_11=Label(frame_21,text="Address",pady=5,padx=20,bg="white",height=2)
        lable_11.grid(row=16,column=0)
        
        date_time=datetime.datetime.now()

        
        tabentry_1=Text(frame_21,width=20,height=1,pady=5,padx=20)
        tabentry_1.grid(row=0,column=4)
        tabentry_2=Text(frame_21,width=20,height=1,pady=5,padx=20)
        tabentry_2.grid(row=2,column=4)
        tabentry_3=Text(frame_21,width=20,height=1,pady=5,padx=20)
        tabentry_3.grid(row=4,column=4)
        tabentry_4=Text(frame_21,width=20,height=1,pady=5,padx=20)
        tabentry_4.grid(row=6,column=4)
        
        tabentry_5=Text(frame_21,width=20,height=1,pady=5,padx=20)
        tabentry_5.grid(row=8,column=4)
        tabentry_5.config(state=DISABLED)
        tabentry_6=Text(frame_21,width=20,height=1,pady=5,padx=20)
        tabentry_6.grid(row=10,column=4)
        tabentry_6.insert(INSERT,date_time)
        tabentry_6.config(state=DISABLED)
        tabentry_7=Text(frame_21,width=20,height=1,pady=5,padx=20)
        tabentry_7.grid(row=12,column=4)
        tabentry_8=Text(frame_21,width=20,height=1,pady=5,padx=20)
        tabentry_8.grid(row=14,column=4)
        tabentry_9=Text(frame_21,width=20,height=1,pady=5,padx=20)
        tabentry_9.grid(row=16,column=4)
        
        frame_21=Frame(frame,width=550,height=450,bg="white",bd=14,padx=150,relief=RIDGE)
        frame_21.grid(row=2,column=2,columnspan=4,sticky="W")
        view_entry=Text(frame_21,width=30,height=25)
        view_entry.grid(row=2,column=2)
        
        frame_3=Frame(frame,width=1370,height=100,bg="white",padx=300,relief=RIDGE,pady=20)
        frame_3.grid(row=5,column=0,columnspan=4,sticky="W")
        def add():
            lable_3.cget("text")
            a=tabentry_1.get("1.0",END)
            
            b=tabentry_2.get("1.0",END)
                
            c=float(tabentry_3.get("1.0",END))
            d=float(tabentry_4.get("1.0",END))
            discount_price=((int(b)*c)*d)/100
            total=int(b)*c-discount_price
            f=str(tabentry_6.get("1.0",END))
            g=str(tabentry_7.get("1.0",END))
            h=str(tabentry_8.get("1.0",END))
            i=str(tabentry_9.get("1.0",END))
            view_entry.insert(END,lable_3.cget("text")+"\t\t:"+a+"\n")
            view_entry.insert(END,lable_4.cget("text")+"\t\t:"+str(b)+"\n")
            view_entry.insert(END,lable_5.cget("text")+"\t\t:"+str(c)+"\n")
            view_entry.insert(END,lable_6.cget("text")+"\t\t:"+str(d)+"\n")
            view_entry.insert(END,lable_7.cget("text")+"\t\t:"+str(total)+"\n")
            view_entry.insert(END,lable_8.cget("text")+"\t\t:"+f+"\n")
            view_entry.insert(END,lable_9.cget("text")+"\t\t:"+g+"\n")
            view_entry.insert(END,lable_10.cget("text")+"\t\t:"+h+"\n")
            view_entry.insert(END,lable_11.cget("text")+"\t\t:"+i)
            

        def clear():
            tabentry_1.delete('1.0', END)
            tabentry_2.delete('1.0', END)
            tabentry_3.delete('1.0', END)
            tabentry_4.delete('1.0', END)
            tabentry_5.delete('1.0', END)
            tabentry_7.delete('1.0', END)
            tabentry_8.delete('1.0', END)
            tabentry_9.delete('1.0', END)
            view_entry.delete('1.0',END)

        def close_window (): 
            window.destroy()

        btn1=Button(frame_3,text="ADD",width=20,pady=10,padx=10,command=add)
        btn1.grid(row=4,column=0,rowspan=10)
        btn2=Button(frame_3,text="SAVE",width=20,pady=10,padx=10)
        btn2.grid(row=4,column=1,rowspan=10)
        btn3=Button(frame_3,text="CLEAR",width=20,pady=10,padx=10,command=clear)
        btn3.grid(row=4,column=2,rowspan=10)
        btn4=Button(frame_3,text="SEARCH",width=20,pady=10,padx=10)
        btn4.grid(row=4,column=3,rowspan=10)
        btn4=Button(frame_3,text="EXIT",width=20,pady=10,padx=10,command=close_window)
        btn4.grid(row=4,column=4,rowspan=10)
        
        label_1=tk.Label(frame_1,text="Purchase Entry",font=40,justify="center",padx=300)
        label_1.grid(row=0,column=0)
        label_2=tk.Label(frame_1,text="Purchase View",font=40,padx=280)
        label_2.grid(row=0,column=3)
        


if __name__ == "__main__":

    window=tk.Tk()
    application=Customer(window)
    window.mainloop()

