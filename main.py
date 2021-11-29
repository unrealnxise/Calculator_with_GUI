from tkinter import *

not_empty = False
not_empty1 = False

number1 = 0
number2 = 0
plus_or_minus = ''

result = 0


def output_clear(event):
    global number1
    global number2
    global plus_or_minus
    global result
    global not_empty1
    global not_empty

    label1["text"] = ''
    label2["text"] = ''
    label3["text"] = ''

    number1 = 0
    number2 = 0
    not_empty = False
    not_empty1 = False
    plus_or_minus = ''
    result = 0


def pr():
    global number1
    global number2
    global plus_or_minus
    global result
    global not_empty
    global not_empty1

    plus_or_minus = ''
    label1["text"] = ''
    label2["text"] = ''
    label3["text"] = str(result)
    not_empty = False
    not_empty1 = False
    number2 = result


def output_result(event):
    global number1
    global number2
    global plus_or_minus
    global result

    if plus_or_minus == '+':
        result = number1 + number2
        pr()
    elif plus_or_minus == '-':
        result = number1 - number2
        pr()
    elif plus_or_minus == '*':
        result = number1 * number2
        pr()
    elif plus_or_minus == '/' and number2 != 0:
        result = number1 / number2
        pr()
    else:
        label1["text"] = ''
        label2["text"] = ''
        label3["text"] = 'Error'


def output1(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '1'
        not_empty = True
        number1 = 1
    elif not not_empty1:
        label3["text"] = '1'
        not_empty1 = True
        number2 = 1


def output2(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '2'
        not_empty = True
        number1 = 2
    elif not not_empty1:
        label3["text"] = '2'
        not_empty1 = True
        number2 = 2


def output3(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '3'
        not_empty = True
        number1 = 3
    elif not not_empty1:
        label3["text"] = '3'
        not_empty1 = True
        number2 = 3


def output4(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '4'
        not_empty = True
        number1 = 4
    elif not not_empty1:
        label3["text"] = '4'
        not_empty1 = True
        number2 = 4


def output5(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '5'
        not_empty = True
        number1 = 5
    elif not not_empty1:
        label3["text"] = '5'
        not_empty1 = True
        number2 = 5


def output6(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '6'
        not_empty = True
        number1 = 6
    elif not not_empty1:
        label3["text"] = '6'
        not_empty1 = True
        number2 = 6


def output7(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '7'
        not_empty = True
        number1 = 7
    elif not not_empty1:
        label3["text"] = '7'
        not_empty1 = True
        number2 = 7


def output8(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '8'
        not_empty = True
        number1 = 8
    elif not not_empty1:
        label3["text"] = '8'
        not_empty1 = True
        number2 = 8


def output9(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '9'
        not_empty = True
        number1 = 9
    elif not not_empty1:
        label3["text"] = '9'
        not_empty1 = True
        number2 = 9


def output0(event):
    global not_empty
    global not_empty1
    global number1
    global number2

    if not not_empty:
        label1["text"] = '0'
        not_empty = True
        number1 = 0
    elif not not_empty1:
        label3["text"] = '0'
        not_empty1 = True
        number2 = 0


def output_plus(event):
    global plus_or_minus

    label2["text"] = '+'
    plus_or_minus = '+'


def output_minus(event):
    global plus_or_minus

    label2["text"] = '-'
    plus_or_minus = '-'


def output_multiply(event):
    global plus_or_minus

    label2["text"] = '*'
    plus_or_minus = '*'


def output_del(event):
    global plus_or_minus

    label2["text"] = '/'
    plus_or_minus = '/'


window = Tk()
window.title('Калькулятор')
window.maxsize(800, 800)
window.minsize(800, 800)

top = Frame(window)
top.pack()

down = Frame(window)
down.pack(side=BOTTOM)

main_text = Label(top, text='Калькулятор', width=45, height=2, font=15)
main_text.grid(row=0, column=2)

label1 = Label(down, width=15, height=5, font=20)
label2 = Label(down, width=15, height=5, font=20)
label3 = Label(down, width=15, height=5, font=20)

button1 = Button(down, width=15, height=5, font=20, text='1', bg='black', fg='white')
button2 = Button(down, width=15, height=5, font=20, text='2', bg='black', fg='white')
button3 = Button(down, width=15, height=5, font=20, text='3', bg='black', fg='white')

button4 = Button(down, width=15, height=5, font=20, text='4', bg='black', fg='white')
button5 = Button(down, width=15, height=5, font=20, text='5', bg='black', fg='white')
button6 = Button(down, width=15, height=5, font=20, text='6', bg='black', fg='white')

button7 = Button(down, width=15, height=5, font=20, text='7', bg='black', fg='white')
button8 = Button(down, width=15, height=5, font=20, text='8', bg='black', fg='white')
button9 = Button(down, width=15, height=5, font=20, text='9', bg='black', fg='white')

button0 = Button(down, width=15, height=5, font=20, text='0', bg='black', fg='white')

button_plus = Button(down, width=15, height=5, font=20, text='+', bg='gray')
button_minus = Button(down, width=15, height=5, font=20, text='-', bg='gray')
button_multiply = Button(down, width=15, height=5, font=20, text='*', bg='gray')
button_del = Button(down, width=15, height=5, font=20, text='/', bg='gray')
button_result = Button(down, width=15, height=5, font=20, text='=', bg='gray')
button_clear = Button(down, width=15, height=5, font=20, text='C', bg='gray')

button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)

button0.grid(row=5, column=1)

button_clear.grid(row=2, column=3)
button_plus.grid(row=4, column=3)
button_minus.grid(row=3, column=3)
button_multiply.grid(row=5, column=0)
button_del.grid(row=5, column=2)
button_result.grid(row=5, column=3)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

button1.bind("<Button-1>", output1)
button2.bind("<Button-1>", output2)
button3.bind("<Button-1>", output3)

button4.bind("<Button-1>", output4)
button5.bind("<Button-1>", output5)
button6.bind("<Button-1>", output6)

button7.bind("<Button-1>", output7)
button8.bind("<Button-1>", output8)
button9.bind("<Button-1>", output9)

button0.bind("<Button-1>", output0)

button_plus.bind("<Button-1>", output_plus)
button_minus.bind("<Button-1>", output_minus)
button_multiply.bind("<Button-1>", output_multiply)
button_del.bind("<Button-1>", output_del)
button_result.bind("<Button-1>", output_result)
button_clear.bind("<Button-1>", output_clear)

window.mainloop()
