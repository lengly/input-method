#-*- coding: utf8 -*-
from Tkinter import *

root = Tk()
root.geometry('250x250')
#标题
label1 = Label(root, text="智能输入法")
label1.pack()
#输出
w1 = PanedWindow(root)
w1.pack()
label2 = Label(w1, text="输出：", fg='blue')
label2.pack(side=LEFT)
outputValue = StringVar()
outputText = Entry(w1, textvariable=outputValue, width=50)
outputText.pack(side=LEFT)
#输入
w2 = PanedWindow(root)
w2.pack()
label3 = Label(w2, text="输入：", fg='blue')
label3.pack(side=LEFT)
inputValue = StringVar()
inputText = Entry(w2, textvariable=inputValue, width=50)
inputText.pack(side=LEFT)
#列表
w3 = PanedWindow(root)
w3.pack()
label4 = Label(w3, text="列表：", fg='blue', height=10)
label4.pack(side=LEFT)
wordList = Text(w3)
wordList.pack(side=LEFT)
