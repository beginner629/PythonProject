import re


def process(read,write):
	f= open(read,'r')
	g= open(write,'w+')

	exampleArray = f.readlines()
	try:
		for i in range(0,len(exampleArray)):

			searchObj = re.search(r'<a href=(.*)>(.*)</a>',exampleArray[i])
			if searchObj:
				if searchObj.group(2)=='Sponsored Links':
					k = re.sub(r'<a href=(.*)>(.*)</a>','',exampleArray[i])

				#print searchObj.group(2)
				else :
					k = re.sub(r'<a href=(.*)>(.*)</a>',searchObj.group(2),exampleArray[i])

			else :
				k=exampleArray[i]
			if k!='':
				print k
				g.write(k+'\n')
	except Exception,e:
		print str(e)

	g.close()
process('/home/revanth/Desktop/Python Stuff/text1.txt','/home/revanth/Desktop/PythonProject/trimmed.txt')