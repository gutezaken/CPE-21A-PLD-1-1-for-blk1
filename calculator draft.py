from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input =StringVar()

txtDisplay = Entry(cal,fg="black",font=('arial', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="silver", justify='right') .grid(columnspan=4)
btn7=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="7",command=lambda:btnClick(7), bg="white") .grid(row=1,column=0)
btn8=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="8",command=lambda:btnClick(8), bg="white") .grid(row=1,column=1)
btn9=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="9",command=lambda:btnClick(9), bg="white") .grid(row=1,column=2)
Addition=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
                text="+", bg="maroon",command=lambda:btnClick("+")) .grid(row=1,column=3)
btn4=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="4",command=lambda:btnClick(4), bg="white") .grid(row=2,column=0)
btn5=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="5",command=lambda:btnClick(5), bg="white") .grid(row=2,column=1)
btn6=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="6",command=lambda:btnClick(6), bg="white") .grid(row=2,column=2)
Subtraction=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
                text="-", bg="orange",command=lambda:btnClick("-")) .grid(row=2,column=3)
btn1=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="1",command=lambda:btnClick(1), bg="white") .grid(row=3,column=0)
btn2=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="2",command=lambda:btnClick(2), bg="white") .grid(row=3,column=1)
btn3=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="3",command=lambda:btnClick(3), bg="white") .grid(row=3,column=2)
Multiply=Button(cal,padx=20,bd=10, fg="black",font=('arial', 20,'bold'),
                text="*", bg="yellow",command=lambda:btnClick("*")) .grid(row=3,column=3)
btn0=Button(cal,padx=20,pady=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="0",command=lambda:btnClick(0), bg="white") .grid(row=4,column=0)
btnClear=Button(cal,padx=20,pady=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="C", bg="indigo",command=btnClearDisplay) .grid(row=4,column=1)
btnEquals=Button(cal,padx=20,pady=20,bd=10, fg="black",font=('arial', 20,'bold'),
            text="=", bg="navy",command=btnEqualsInput) .grid(row=4,column=2)
Division=Button(cal,padx=20,pady=20,bd=10, fg="black",font=('arial', 20,'bold'),
                text="/", bg="green",command=lambda:btnClick("/")) .grid(row=4,column=3)

cal.mainloop()
