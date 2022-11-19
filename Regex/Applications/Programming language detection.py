import re
import sys
str_code=''.join(sys.stdin.readlines())
pattern1=r'java\.|static\svoid\smain'
pattern2=r'\#include\<\w+'
if re.search(pattern1,str_code) is not None:
    print('Java')
elif re.search(pattern2,str_code) is not None:
    print('C')
else:
    print('Python')
