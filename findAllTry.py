import re


#speechForm='IN'
f= open('/home/revanth/Desktop/PythonProject/analyzing.txt','r',10)
g= open('/home/revanth/Desktop/PythonProject/words.txt','w+',10)
para= f.readlines()
f.close()

for text in para:
	nouns= re.findall(r"('[\w]*', '[NNP]')",text)
	if nouns:
		#print nouns
		for word in nouns:
			reqWord= re.search(r"'([\w]*)', '[NNP]'",word).group(1)
			if reqWord:
				g.write(reqWord)



#print nouns[0]

string = "Once you have accomplished small things, you may attempt great ones safely."

# Return all words beginning with character 'a', as a list of strings
#print re.findall(r"\ba[\w]*", string)