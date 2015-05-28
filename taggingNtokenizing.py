import nltk
import re


f=open('/home/revanth/Desktop/PythonProject/trimmed.txt','r')

temp=f.readline()
text=[]
count=0
while temp:
	if temp=="\n": count+=1
	else: text.append(temp)
	temp=f.readline()

tokenized=[]
chunkGram = r"""Chunk: {(<NNP?S?>|<IN>)} 
							}<NNP?S?>+{"""
chunkParser=nltk.RegexpParser(chunkGram)

def taggerNtokenizer(line):
	tokenized.append(nltk.word_tokenize(line))
	tagged = nltk.pos_tag(tokenized[-1])
	chunked = chunkParser.parse(tagged)
	print chunked

	
	print
	print

for line in text:
	if line:
		if line=='':
			continue
		else:taggerNtokenizer(line)
#print tokenized
