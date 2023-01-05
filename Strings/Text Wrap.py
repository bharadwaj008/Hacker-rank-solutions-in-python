def wrap(string, max_width):
    
    
    #divided the string as substrings of length=max_width
    #then attached appended them to list using list comprehension
    lst=[string[max_width*i:max_width*(i+1)] for i in range(0,(len(string)//max_width)+1)]
    
    
    #joining the list of substrings using join method with
    #'\n' as the seperator to print them in consecutive lines
    str1='\n'.join(lst)
    
        
    return str1

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)