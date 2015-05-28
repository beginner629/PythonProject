

f = open('/home/revanth/Desktop/PythonProject/words.txt', 'r', 10)
mylist = f.readlines()
words = []
count = []
maxpos = []

flag = 0
for word in mylist:
    if len(words) == 0:
        words.append(word)
        count.append(1)
        flag = 1
    else:
        for i in range(0, len(words)):
            flag = 0
            if words[i] == word:
                count[i] += 1
                flag = 1
                break
    if flag == 0:
        words.append(word)
        count.append(1)


#for i in range(0, len(words)):
    #print str(count[i])+'   '+words[i]
    # print


maxi = 0
for i in range(0, len(count)):
    if count[i] > maxi:
        maxi = count[i]
        maxpos = [i]
    elif count[i] == maxi:
        maxpos.append(i)

maxwords = []
for i in range(0, len(maxpos)):
    maxwords.append(words[maxpos[i]])

print maxi
print
for word in maxwords:
	print word
# print 'done'
