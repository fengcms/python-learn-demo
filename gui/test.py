from tkinter import *
import sys
import getpw
import clipboard

root = Tk()
root.title('密码生成器')
leng = StringVar()
leng.set(8)

f1 = Frame(root)
f1.pack(padx=10,pady=5)
f2 = Frame(root)
f2.pack(padx=10,pady=5)

def test(res):
    print(res)
    if res.isdigit():
        return int(res) > 4
    else:
        return False

testCMD = root.register(test)

Label(f1, text="密码长度：").grid(row=0,column=0)

f1r = Frame(f1)
f1r.grid(row=0, column=1)

e1 = Entry(f1r, textvariable=leng, width=5, validate="key",validatecommand=(testCMD, '%P')).grid(row=0,column=1)

def calcPlus():
    leng.set(int(leng.get()) + 1)

def calcSubt():
    lengVal = int(leng.get())
    if lengVal > 4:
        leng.set(lengVal - 1)

Button(f1r, text="+", command=calcPlus).grid(row=0, column=2)
Button(f1r, text="-", command=calcSubt).grid(row=0, column=3)

level = IntVar()
level.set(3)

Label(f1, text="密码强度：").grid(row=1,column=0)

f1rb = Frame(f1)
f1rb.grid(row=1, column=1)

Radiobutton(f1rb, text="简单", variable=level, value=1).grid(row=1, column=1)
Radiobutton(f1rb, text="一般", variable=level, value=3).grid(row=1, column=2)
Radiobutton(f1rb, text="复杂", variable=level, value=4).grid(row=1, column=3)

pw = StringVar()
Entry(root,textvariable=pw,state="readonly").pack()

def getPw():
    res = getpw.getPassword(int(leng.get()),level.get())
    clipboard.copy(res)
    pw.set(res)
submit = Button(root,text="生成密码并复制到剪切板", command=getPw)
submit.pack()

mainloop()
