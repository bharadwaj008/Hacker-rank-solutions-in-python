import re

N = int(input())
test_list = [input() for _ in range(N)]

test_string = '\n'.join(test_list)
#print(test_string)

for _ in range(int(input())):
    print(len(re.findall(rf'\b{input()}\b', test_string)))
