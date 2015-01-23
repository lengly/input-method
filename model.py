class Model:
	def __init__(self):
		self.words = []
		self.page = 0
	def pager(self):
		return self.words[(self.page * 10) : ((self.page+1) * 10)]
	def prev(self):
		if self.page>0:
			self.page -= 1
	def next(self):
		if len(self.words)/10 > self.page:
			self.page += 1
		print('now page is %d' %self.page)
	def query(self, key, dictionary):
		while (len(key)>0 and key[-1].isalpha()==False):
			key = key[:-1]
		if key in dictionary:
			self.words = dictionary[key]
		else:
			self.words = []
		self.page = 0
