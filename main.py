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

dictionary = load_dictionary()
print '字典读入完毕'

m = model.Model()

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
			else : num = int(key) - 1
			result = m.pager()[num]
			UI.outputValue.set(UI.outputValue.get() + result.decode('utf8'))
			UI.inputValue.set('')
		m.query(UI.inputValue.get(), dictionary)
	show(UI.wordList)

UI.inputText.bind("<KeyRelease>", key)

UI.root.mainloop()
