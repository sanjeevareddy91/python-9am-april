# # tkinter --- Its a library for bulding the desktop applications..


# from tkinter import Tk,Button,Frame,Label,StringVar
# # Step1: Creating the Screen of the calculator.

# # root = tkinter.Tk()

# # root.mainloop()


# # Step2: Lets give the dimensions to stick the screen at fixed location..


# # root = tkinter.Tk()

# # root.geometry('450x450+300+100')

# # root.resizable(0,0)

# # root.title("Calculator")
# # root.mainloop()


# # Step3: Dividing the screen in 4 different frames..

# # root = tkinter.Tk()

# # root.geometry('450x450+300+100')

# # root.resizable(0,0)

# # root.title("Calculator")



# # frame1 = Frame(root,bg='red')
# # frame1.pack(fill='both',expand=True)

# # frame2 = Frame(root,bg='green')
# # frame2.pack(fill='both',expand=True)

# # frame3 = Frame(root,bg='blue')
# # frame3.pack(fill='both',expand=True)

# # frame4 = Frame(root,bg='black')
# # frame4.pack(fill='both',expand=True)


# # btn1 = Button(frame1,text="1",font=('Verdana',20),border=0)
# # btn1.pack(expand=True,fill="both",side='left')


# # btn2 = Button(frame1,text="2",font=('Verdana',20),border=0)
# # btn2.pack(expand=True,fill="both",side='left')

# # btn3 = Button(frame1,text="3",font=('Verdana',20),border=0)
# # btn3.pack(expand=True,fill="both",side='left')

# # btnplus = Button(frame1,text="+",font=('Verdana',20),border=0)
# # btnplus.pack(expand=True,fill="both",side='left')


# # btn4 = Button(frame2,text="4",font=('Verdana',20),border=0)
# # btn4.pack(expand=True,fill="both",side='left')


# # btn5 = Button(frame2,text="5",font=('Verdana',20),border=0)
# # btn5.pack(expand=True,fill="both",side='left')

# # btn6 = Button(frame2,text="6",font=('Verdana',20),border=0)
# # btn6.pack(expand=True,fill="both",side='left')

# # btnminus = Button(frame2,text="-",font=('Verdana',20),border=0)
# # btnminus.pack(expand=True,fill="both",side='left')


# # btn7 = Button(frame3,text="7",font=('Verdana',20),border=0)
# # btn7.pack(expand=True,fill="both",side='left')


# # btn8 = Button(frame3,text="8",font=('Verdana',20),border=0)
# # btn8.pack(expand=True,fill="both",side='left')

# # btn9 = Button(frame3,text="9",font=('Verdana',20),border=0)
# # btn9.pack(expand=True,fill="both",side='left')

# # btnmul = Button(frame3,text="*",font=('Verdana',20),border=0)
# # btnmul.pack(expand=True,fill="both",side='left')


# # btnC = Button(frame4,text="C",font=('Verdana',20),border=0)
# # btnC.pack(expand=True,fill="both",side='left')


# # btn0 = Button(frame4,text="0",font=('Verdana',20),border=0)
# # btn0.pack(expand=True,fill="both",side='left')

# # btnequal = Button(frame4,text="=",font=('Verdana',20),border=0)
# # btnequal.pack(expand=True,fill="both",side='left')

# # btndiv = Button(frame4,text="/",font=('Verdana',20),border=0)
# # btndiv.pack(expand=True,fill="both",side='left')

# # root.mainloop()


# # Step4: Creating the Label for the calculator..
# # root = Tk()

# # root.geometry('450x450+300+100')

# # root.resizable(0,0)

# # root.title("Calculator")

# # label_data = Label(root,text="This is Label",anchor='se',font=('Verdana',20))
# # label_data.pack(expand=True,fill='both')

# # frame1 = Frame(root,bg='red')
# # frame1.pack(fill='both',expand=True)

# # frame2 = Frame(root,bg='green')
# # frame2.pack(fill='both',expand=True)

# # frame3 = Frame(root,bg='blue')
# # frame3.pack(fill='both',expand=True)

# # frame4 = Frame(root,bg='black')
# # frame4.pack(fill='both',expand=True)


# # btn1 = Button(frame1,text="1",font=('Verdana',20),border=0)
# # btn1.pack(expand=True,fill="both",side='left')


# # btn2 = Button(frame1,text="2",font=('Verdana',20),border=0)
# # btn2.pack(expand=True,fill="both",side='left')

# # btn3 = Button(frame1,text="3",font=('Verdana',20),border=0)
# # btn3.pack(expand=True,fill="both",side='left')

# # btnplus = Button(frame1,text="+",font=('Verdana',20),border=0)
# # btnplus.pack(expand=True,fill="both",side='left')


# # btn4 = Button(frame2,text="4",font=('Verdana',20),border=0)
# # btn4.pack(expand=True,fill="both",side='left')


# # btn5 = Button(frame2,text="5",font=('Verdana',20),border=0)
# # btn5.pack(expand=True,fill="both",side='left')

# # btn6 = Button(frame2,text="6",font=('Verdana',20),border=0)
# # btn6.pack(expand=True,fill="both",side='left')

# # btnminus = Button(frame2,text="-",font=('Verdana',20),border=0)
# # btnminus.pack(expand=True,fill="both",side='left')


# # btn7 = Button(frame3,text="7",font=('Verdana',20),border=0)
# # btn7.pack(expand=True,fill="both",side='left')


# # btn8 = Button(frame3,text="8",font=('Verdana',20),border=0)
# # btn8.pack(expand=True,fill="both",side='left')

# # btn9 = Button(frame3,text="9",font=('Verdana',20),border=0)
# # btn9.pack(expand=True,fill="both",side='left')

# # btnmul = Button(frame3,text="*",font=('Verdana',20),border=0)
# # btnmul.pack(expand=True,fill="both",side='left')


# # btnC = Button(frame4,text="C",font=('Verdana',20),border=0)
# # btnC.pack(expand=True,fill="both",side='left')


# # btn0 = Button(frame4,text="0",font=('Verdana',20),border=0)
# # btn0.pack(expand=True,fill="both",side='left')

# # btnequal = Button(frame4,text="=",font=('Verdana',20),border=0)
# # btnequal.pack(expand=True,fill="both",side='left')

# # btndiv = Button(frame4,text="/",font=('Verdana',20),border=0)
# # btndiv.pack(expand=True,fill="both",side='left')

# # root.mainloop()



# # Step5: Writing the funcationality for buttons and Displaying the label with values..

# root = Tk()

# root.geometry('450x450+300+100')

# root.resizable(0,0)

# root.title("Calculator")


# data = StringVar() # This is just for showing the data on the label..

# val = "" # this is for storing the result to the varibale..

# def btn1_isclicked():
#     global val
#     val = val + "1" # '' + '1' =>> '1'
#     data.set(val)

# def btn2_isclicked():
#     global val
#     val = val + "2" # '' + '1' =>> '1'
#     data.set(val)

# def btn3_isclicked():
#     global val
#     val = val + "3" # '' + '1' =>> '1'
#     data.set(val)

# def btn4_isclicked():
#     global val
#     val = val + "4" # '' + '1' =>> '1'
#     data.set(val)

# def btn5_isclicked():
#     global val
#     val = val + "5" # '' + '1' =>> '1'
#     data.set(val)

# def btn6_isclicked():
#     global val
#     val = val + "6" # '' + '1' =>> '1'
#     data.set(val)

# def btn7_isclicked():
#     global val
#     val = val + "7" # '' + '1' =>> '1'
#     data.set(val)

# def btn8_isclicked():
#     global val
#     val = val + "8" # '' + '1' =>> '1'
#     data.set(val)

# def btn9_isclicked():
#     global val
#     if val.startswith('0'):
#         val = val[1:]
#     val = val + "9" # '' + '1' =>> '1'
#     data.set(val)

# def btn0_isclicked():
#     global val
#     val = val + "0" # '' + '1' =>> '1'
#     data.set(val)

# def btnadd_isclicked():
#     global val
#     val = val + "+" # '' + '1' =>> '1'
#     data.set(val)

# def btnsub_isclicked():
#     global val
#     val = val + "-" # '' + '1' =>> '1'
#     data.set(val)

# def btnmul_isclicked():
#     global val
#     val = val + "*" # '' + '1' =>> '1'
#     data.set(val)

# def btndiv_isclicked():
#     global val
#     val = val + "/" # '' + '1' =>> '1'
#     data.set(val)

# def btnC_isclicked():
#     global val
#     val = '0' # '' + '1' =>> '1'
#     data.set(val)


# def btnequal_isclicked():
#     # (1+3)*3+(4*5)
#     global val
#     val = eval(val)
#     val = str(val)
#     data.set(val)

# label_data = Label(root,text="This is Label",anchor='se',font=('Verdana',20),textvariable=data)
# label_data.pack(expand=True,fill='both')

# frame1 = Frame(root,bg='red')
# frame1.pack(fill='both',expand=True)

# frame2 = Frame(root,bg='green')
# frame2.pack(fill='both',expand=True)

# frame3 = Frame(root,bg='blue')
# frame3.pack(fill='both',expand=True)

# frame4 = Frame(root,bg='black')
# frame4.pack(fill='both',expand=True)


# btn1 = Button(frame1,text="1",font=('Verdana',20),border=0,command=btn1_isclicked)
# btn1.pack(expand=True,fill="both",side='left')


# btn2 = Button(frame1,text="2",font=('Verdana',20),border=0,command=btn2_isclicked)
# btn2.pack(expand=True,fill="both",side='left')

# btn3 = Button(frame1,text="3",font=('Verdana',20),border=0,command=btn3_isclicked)
# btn3.pack(expand=True,fill="both",side='left')

# btnplus = Button(frame1,text="+",font=('Verdana',20),border=0,command=btnadd_isclicked)
# btnplus.pack(expand=True,fill="both",side='left')


# btn4 = Button(frame2,text="4",font=('Verdana',20),border=0,command=btn4_isclicked)
# btn4.pack(expand=True,fill="both",side='left')


# btn5 = Button(frame2,text="5",font=('Verdana',20),border=0,command=btn5_isclicked)
# btn5.pack(expand=True,fill="both",side='left')

# btn6 = Button(frame2,text="6",font=('Verdana',20),border=0,command=btn6_isclicked)
# btn6.pack(expand=True,fill="both",side='left')

# btnminus = Button(frame2,text="-",font=('Verdana',20),border=0,command=btnsub_isclicked)
# btnminus.pack(expand=True,fill="both",side='left')


# btn7 = Button(frame3,text="7",font=('Verdana',20),border=0,command=btn7_isclicked)
# btn7.pack(expand=True,fill="both",side='left')


# btn8 = Button(frame3,text="8",font=('Verdana',20),border=0,command=btn8_isclicked)
# btn8.pack(expand=True,fill="both",side='left')

# btn9 = Button(frame3,text="9",font=('Verdana',20),border=0,command=btn9_isclicked)
# btn9.pack(expand=True,fill="both",side='left')

# btnmul = Button(frame3,text="*",font=('Verdana',20),border=0,command=btnmul_isclicked)
# btnmul.pack(expand=True,fill="both",side='left')


# btnC = Button(frame4,text="C",font=('Verdana',20),border=0,command=btnC_isclicked)
# btnC.pack(expand=True,fill="both",side='left')


# btn0 = Button(frame4,text="0",font=('Verdana',20),border=0,command=btn0_isclicked)
# btn0.pack(expand=True,fill="both",side='left')

# btnequal = Button(frame4,text="=",font=('Verdana',20),border=0,command=btnequal_isclicked)
# btnequal.pack(expand=True,fill="both",side='left')

# btndiv = Button(frame4,text="/",font=('Verdana',20),border=0,command=btndiv_isclicked)
# btndiv.pack(expand=True,fill="both",side='left')

root.mainloop()
