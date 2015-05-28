#from BeautifulSoup import BeautifulSoup, NavigableString

import nltk
#import re
import time


class Nouns:
	name = ''
	count=0

	def __init__ (self,name,):
		self.name = name
		self.count= 1

	def __repr__(self):
		return 'Nouns name:%s count:%s' % (self.name, self.count)

	def __str__(self):
		return self.name + '  ' + self.count

	def __getdata__(self):
		print self.name + '   ' + self.count

f= open('/home/revanth/Desktop/PythonProject/trimmed.txt','r')
g= open('/home/revanth/Desktop/PythonProject/analyzing.txt','w+')

exampleArray = f.readlines()

popList = []
def processLanguage():

	i = 0
	popped=0
	j=len(exampleArray)/2
	#print j
	chunks = [None] * j
	#SomeList = [None] * j
	try:
		for i in range(0,2):


			if exampleArray[2*i] is None:
				popped+=1	
			else :


				tokenized = nltk.word_tokenize(exampleArray[2*i])
				#print tokenized
				tagged = nltk.pos_tag(tokenized)
				#SomeList[i-popped] = tokenized
				#print tagged
				chunkGram = r"""Chunk: {<NNP?S?>*<NNP?S?>}"""
				chunkParser=nltk.RegexpParser(chunkGram)

				chunked = chunkParser.parse(tagged)
				chunks [i-popped]=chunked

				
				#print chunks[i-popped]
				g.write(str(tagged))
				g.write('\n')
				print chunked
				
				#i=1+i
				#chunked.draw()


			#time.sleep(555)



	except Exception,e:
		print str(e)

	#print 'This is a break'
	parseList=[]
	#parseList.append(Nouns(SomeList[0][0]))
	
	#print 'Some text'
	#print popped


	#for chunk in chunks[0]

processLanguage()

f.close()
g.close()