import re


# speechForm='IN'
f = open('/home/revanth/Desktop/PythonProject/analyzing.txt', 'r', 10)
#g = open('/home/revanth/Desktop/Python Trials/words.txt', 'w+', 10)
para1 = f.readlines()
# f.close()
#para1 = [('John', 'NNP'), ('Bercow', 'NNP'), ('will', 'MD'), ('be', 'VB'), ('installed', 'VBN'), ('unopposed', 'VBN'), ('as', 'IN'), ('Speaker', 'NNP'), ('of', 'IN'), ('the', 'DT'), ('House', 'NNP'), ('of', 'IN'), ('Commons', 'NNPS'), ('tomorrow', 'NN'), ('(', ':'), ('Monday', 'NNP'), (')', ':'), ('after', 'IN'), ('Tory', 'NNP'), ('backbenchers', 'NNS'), ('agreed', 'VBD'), ('not', 'RB'), ('to', 'TO'), ('object', 'VB'), ('to', 'TO'), ('his', 'PRP$'), ('re-election', 'NN'), ('.', '.')]
nouns = []
#speechpart='NNP'
speechparts=['NNP', 'IN', 'DT', 'NNP']
#regHead=r"\('[\w]*', '"
#regMid=r"'\), \('[\w]*', '"
#regTail=r"'\)"
regHead=r"\('([\w]*?)', '"
regMid=r"'\), \('([\w]*?)', '"
regTail=r"'\)"

myRegex=regHead+re.escape(speechparts[0])
for i in range(1,len(speechparts)):
	myRegex+=regMid+re.escape(speechparts[i])
myRegex+=regTail

#myRegex=r"\('[\w]*', '"+ re.escape(speechpart) +r"'\), \('[\w]*', '"+re.escape(speechpart)+r"'\)"
#myRegex=ur"\('(.+?)', 'NNP'\), \('(.+?)', 'NNP'\)"
#myRegex=ur"\('(.+?)', 'NNP'\)+?"
for text in para1:
	para2 = str(text)
	nouns.append(re.findall(myRegex, para2))

    #noun1= re.findall(r"('[\w]*', 'CD'), ('[\w]*', 'NNS')",text)
for parts in nouns:
	if parts:
		for part in parts:
			print part
#print nouns
	#else :
		#pass
	#print nouns

# print nouns[0]
# Return all words beginning with character 'a', as a list of strings
# print re.findall(r"\ba[\w]*", string)