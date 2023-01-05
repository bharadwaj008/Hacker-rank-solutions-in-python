def print_formatted(number):
    
    #as bin(number) produces output '0bxxxx'. So to get
    #the exact length of binary value of the number we r 
    #doing '-2' from len(bin(number))
    
    len_of_bin_no=len(bin(number))-2
    
    #making a for loop from 1 to number using range function
    #as second parameter is excluded from list of number using
    #number+1 as second parameter
    
    for i in range(1,number+1):
        
        #As decimal number is int data type we r converting
        #it to the string using str() funtion and using rjust
        #to right justify it and gave the above defined len_of
        #_bin_no as input for .rjust() method
        deci=str(i).rjust(len_of_bin_no)
        
        #As asked in question to get octal of number we can use
        #in-built function oct() and it produces output like
        #0oxxxx we use string slicing to start from 3rd character
        #and used rjust to right-justified and gave len_of_bin_no
        #as parameter
        octal=(oct(i)[2:]).rjust(len_of_bin_no)
        
        #As asked in question to get  of number we can use
        #in-built function hex() and it produces output like
        #0xxxxx we use string slicing to start from 3rd character
        #and convert it to the upper case used .upper() method,then used rjust to right-justified and gave 
        # len_of_bin_no as parameter.
        hexa=((hex(i).upper())[2:]).rjust(len_of_bin_no)
        
        #As asked in question to get binary of number we can use
        #in-built function bin() and it produces output like
        #0bxxxx we use string slicing to start from 3rd character
        #and used rjust to right-justified and gave len_of_bin_no
        #as parameter
        binary=(bin(i)[2:]).rjust(len_of_bin_no)
        
        #formed the list from above formatted strings of deci,octal,hexa,binary
        lst=[deci,octal,hexa,binary]
        
        #instead of using the for loop to print the list ofvalues,
        #we can *listname and give sep parameter input to seperate the list values
        print(*lst,sep=' ')
        
        
        
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)