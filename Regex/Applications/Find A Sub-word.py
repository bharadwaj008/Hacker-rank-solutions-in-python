import re
#taking input of no.of sentences
n=int(input())
'''initializing list to store the input sentences to search for query words''' 
lst_sen=[]
#appending inputs to the list thru for loop
for i in range(n):
    lst_sen.append(input())
#taking input of no.of sub-words(queries)
qno=int(input())
'''initializing list to store the input query words to search in sentences'''
qlst=[]
#appending query words inputs to the list thru for loop
#forming the regular expression while taking the input
for _ in range(qno):
    input_word=input()
    pattern=rf'\w{input_word}\w'
    qlst.append(pattern) 

#looping thru our list of patterns and find it,s matchings in #every sentence. here we an loop thru the sentences using inner #loop or use join method of string

for pat in qlst:
    out=0
    print(len(re.findall(pat,"\n".join(lst_sen))))
    '''for sen in lst_sen:
        ou=re.findall(pat,sen)
        out += len(ou)
    print(out)'''
    