import re

#taking input of no.of lines
n=int(input())

#forming IPv4 pattern as we can have integer from 0-255. Here[0-9] forms all single digits next [1-9][0-9] forms
#10-99, next [1][0-9][0-9] forms 100-199 , next [2][0-5][0-5] forms 200-255 and added '.' for all matches.
pattern1=r'([0-9]\.|[1-9][0-9]\.|[1][0-9][0-9]\.|[2][0-5][0-5]\.){4}'

#forming IPv6 pattern as we can have 4 characters which are 0-9 and a-f next i included 1,2,3 because as it is
#given in question that An IPv6 value such as "...:0:..." or "...:5:..." is address-wise identical to "...:0000:..." or "...:0005:....". 
# Leading zeros may be omitted in writing the address.
pattern2=r'(([0-9a-f]){4}\:|[0-9a-f]\:|[0-9a-f]{2}\:|[0-9a-f]{3}\:){8}'

#finally taking input of all addresses to validate them but there is a small catch here,i.e as we have added
#'.' and ':' for every part of the match but last part won't have that character. So,after input we have added
#them and check for the pattern

for i in range(n):
    int_str=input()
    if '.' in int_str:
        int_str+='.'
        match=re.search(pattern1,int_str)
        if match is not None:
            print('IPv4')
        else:
            print('Neither')
    elif ':' in int_str:
            int_str+=':'
            match=re.search(pattern2,int_str)
            if match is not None:
                print('IPv6')
            else:
                print('Neither')
    else:
        print('Neither')