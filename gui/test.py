from tkinter import *

root = Tk()

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
e1 = Entry(f1, textvariable=leng, width=5, validate="key",validatecommand=(testCMD, '%P')).grid(row=0,column=1)

def calcPlus():
    leng.set(int(leng.get()) + 1)

def calcSubt():
    lengVal = int(leng.get())
    if lengVal > 4:
        leng.set(lengVal - 1)

Button(f1, text="+", command=calcPlus).grid(row=0, column=2)
Button(f1, text="-", command=calcSubt).grid(row=0, column=3)

level = IntVar()
level.set(3)

Label(f1, text="密码强度：").grid(row=1,column=0)

Radiobutton(f1, text="简单", variable=level, value=1).grid(row=1, column=1)
Radiobutton(f1, text="一般", variable=level, value=3).grid(row=1, column=2)
Radiobutton(f1, text="复杂", variable=level, value=4).grid(row=1, column=3)

submit = Button(root,text="生成密码并复制到剪切板")
submit.pack()
mainloop()
