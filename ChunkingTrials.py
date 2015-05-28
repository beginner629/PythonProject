import re


# speechForm='IN'
f = open('/home/revanth/Desktop/PythonProject/analyzing.txt', 'r', 10)
#g = open('/home/revanth/Desktop/Python Trials/words.txt', 'w+', 10)
para1 = f.readlines()
# f.close()
para = [('John', 'NNP'), ('Bercow', 'NNP'), ('will', 'MD'), ('be', 'VB'), ('installed', 'VBN'), ('unopposed', 'VBN'), ('as', 'IN'), ('Speaker', 'NNP'), ('of', 'IN'), ('the', 'DT'), ('House', 'NNP'), ('of', 'IN'), ('Commons', 'NNPS'), ('tomorrow', 'NN'), ('(', ':'), ('Monday', 'NNP'), (')', ':'), ('after', 'IN'), ('Tory', 'NNP'), ('backbenchers', 'NNS'), ('agreed', 'VBD'), ('not', 'RB'), ('to', 'TO'), ('object', 'VB'), ('to', 'TO'), ('his', 'PRP$'), ('re-election', 'NN'), ('.', '.')]


nouns = []
speechpart='NNP'
#regHead=r"\('[\w]*', '"
#regMid=r"'\), \('[\w]*', '"
#regTail=r"'\)"
#myRegex=regHead+re.escape(speechpart)+regMid
#myRegex+=re.escape(speechpart)+regTail
#myRegex=r"\('[\w]*', '"+ re.escape(speechpart) +r"'\), \('[\w]*', '"+re.escape(speechpart)+r"'\)"
myRegex=r"\('([a-zA-Z]+?)', 'NNP'\), \('([a-zA-Z]+?)', 'NNS'\), \('([a-zA-Z]+?)', 'VBD'\)+?"
#myRegex=ur"\('([a-zA-Z]+?)', 'NNP'\)+?"
for i in range(0,len(para1)):
	para2 = str(para1[i])
	nouns.append(re.findall(myRegex, para2))
#para2=str(para)
#nouns.append(re.findall(myRegex, para2))
    #noun1= re.findall(r"('[\w]*', 'CD'), ('[\w]*', 'NNS')",text)
for parts in nouns:
	if parts:
		for part in parts:
			print part
			#pass
	#else :
		#pass
#print nouns
#print para
#print para1[0]
# print nouns[0]
# Return all words beginning with character 'a', as a list of strings
# print re.findall(r"\ba[\w]*", string)