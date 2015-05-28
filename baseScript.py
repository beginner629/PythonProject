import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders=[('User-agent','Mozilla/5.0')]
g= open('/home/revanth/Desktop/PythonProject/matter.txt','w+')

def main():
	try:
		page = 'http://www.huffingtonpost.co.uk/feeds/index.xml'
		sourceCode = opener.open(page).read()
		#print sourceCode

		try:
			titles = re.findall(r'<title><!\[CDATA\[(.*?)]]></title>',sourceCode)
			links  = re.findall(r'<link>(.*?)</link>',sourceCode)
			for title in titles:
				print title
				print

			for link in links:
				print link
				print 

			for i in range(len(titles)):
				print titles[i]
				print links[i+1]
				print

			for link in links:
				if link=='www.huffingtonpost.co.uk':
					pass
				else:
					linkSource = opener.open(link).read()
				#print linkSource
					content = re.findall(r'<p>(.*?)</p>',linkSource)
					for theContent in content:
						print theContent
						g.write(theContent)
						g.write('\n\n')
					g.write('\n\n\n\n\n\n\n')



		except Exception, e:
			print str(e)

	except Exception, e:
			print str(e)

main()
g.close()