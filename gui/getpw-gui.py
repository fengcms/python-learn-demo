from tkinter import *
import sys
import clipboard
import random

def cutLength(leng, level):
    res = []
    for i in range(level, 1, -1):
        res.append(random.randint(1, leng - sum(res) - i + 1))
    res.append(leng - sum(res))
    random.shuffle(res)
    return res

def makePassword(dists, arr):
    res = []
    for i in range(len(arr)):
        for j in range(arr[i]):
            res += random.choice(dists[i])
    random.shuffle(res)
    return ''.join(res)

def getPassword(leng, level):
    arr = cutLength(leng,level)
    str1 = '01'
    str2 = '23456789'
    str3 = 'abcdefghijkmnpqrstuvwxyz'
    str4 = 'ABCDEFGHJKMNPQRSTUVWXYZ'
    str5 = '_@!,.:;-=+/?'

    dists = {
        1: [str1 + str2],
        3: [str2, str3, str4],
        4: [str2, str3, str4, str5]
    }
    return makePassword(dists[level], arr)

def test(res):
    if res.isdigit():
        return int(res) > 4
    else:
        return False

def calcPlus():
    leng.set(int(leng.get()) + 1)

def calcSubt():
    lengVal = int(leng.get())
    if lengVal > 4:
        leng.set(lengVal - 1)

def getPw():
    res = getPassword(int(leng.get()),level.get())
    clipboard.copy(res)
    pw.set(res)

if __name__ == "__main__":
    root = Tk()
    root.title('密码生成器')
    leng = StringVar()
    leng.set(8)

    f1 = Frame(root)
    f1.pack(padx=10,pady=5)

    testCMD = root.register(test)

    Label(f1, text="密码长度：").grid(row=0,column=0)

    f1r = Frame(f1)
    f1r.grid(row=0, column=1)

    e1 = Entry(f1r, textvariable=leng, width=5, validate="key",validatecommand=(testCMD, '%P')).grid(row=0,column=1)


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

    submit = Button(root,text="生成密码并复制到剪切板", command=getPw)
    submit.pack()

    mainloop()
