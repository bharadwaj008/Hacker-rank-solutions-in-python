#This code is my version of solution for UK and US: part-2 in regular expression of hackerrank
#importing regular expressions module 
import re
#taking input of no..of sentences
n=int(input())
#appending inputs to the empty list using list comprehension
sens=[input() for _ in range(n)]
#taking input of no.of words to search in the above
#sentences list
nw=int(input())
for i in range(nw):
    hpatt=input()
    #we want to find for the u followed by r,,so i am using this 
    #pattern
    rpatt=r'u(?=r)'
    #Then substituting the u followed by r with empty space to 
    #form the us spelling of a word 
    hpatt1=''.join(re.sub(rpatt,'',hpatt))
    #print(hpatt1,hpatt)
    #then finally this is the required pattern to search in the 
    #sentences. Instead of looping in the sentences i used join
    #method here
    patt=rf'{hpatt1}\b|{hpatt}\b'
    ot=len(re.findall(patt,' '.join(sens)))
    print(ot)