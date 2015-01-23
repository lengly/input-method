#-*- coding: utf8 -*-
import UI
import model

def load_dictionary():
    d = {}
    with open("dict.txt","r") as f:
        for line in f.read().split('\n'):
            if line.startswith("#"):continue
            else:
                items=line.split(" ")
                if len(items)<1:continue
                value = items[0]
                for key in items[1:]:
                    if key in d:
                        d[key].append(value)
                    else:
                        d[key] = [value]
    return d

def load_words(dictionary):
    #构造逆字典   汉字＝>拼音
    reversedDict = {}
    for key,values in dictionary.items():
        for value in values:
            if value in reversedDict:
                reversedDict[value].append(key)
            else:
                reversedDict[value] = [key]
    #读入词库
    with open("words.txt","r") as f:
        for line in f.read().split('\n'):
            for word in line.split('\t'):
                values = [[]]
                for i in range(len(word)/3):
                    singleWord = word[i*3:i*3+3]
                    value = values[:]
                    values = []
                    for p in reversedDict[singleWord]:
                        values.extend([w+[p] for w in value])
                for keys in values:
                    key = ''.join(keys)
                    if key in dictionary:
                        dictionary[key].append(word)
                    else:
                        dictionary[key] = [word]

def show(wordList):
    wordList.delete(1.0, UI.END)
    if m.words:
        newWords = ['%d  %s' % ((i+1)%10,x) for i,x in enumerate(m.pager())]
        for s in newWords:
            wordList.insert(UI.END, s+'\n')

def key(event):
    key = event.keysym
    print key
    if key == 'space': key = '1'
    if key == 'minus':
        m.prev()
        UI.inputValue.set(UI.inputValue.get()[:-1])
    elif key == 'equal':
        m.next()
        UI.inputValue.set(UI.inputValue.get()[:-1])
    else:
        if key in '1234567890':
            if key == '0': num = 9
            else: num = int(key) - 1
            result = m.pager()[num]
            UI.outputValue.set(UI.outputValue.get() + result.decode('utf8'))
            s = UI.inputValue.get()
            t = reversedDict[result]
            for i in t:
                if s.startswith(i):
                    s = s[len(i):-1]
                    break
            UI.inputValue.set(s)
        m.query(UI.inputValue.get(), dictionary)
    show(UI.wordList)

UI.inputText.bind("<KeyRelease>", key)

dictionary = load_dictionary()
print '字典加载完毕'
load_words(dictionary)
print '词组加载完毕'
print '字典长度：%d' % len(dictionary)
reversedDict = {}
for key,values in dictionary.items():
    for value in values:
        if value in reversedDict:
            reversedDict[value].append(key)
        else:
            reversedDict[value] = [key]
m = model.Model()



UI.root.mainloop()
