start_Number = 0   #first sample number to start with

iterator = 0     # iterator determines how many times the loop executes

n = 6            # empty string iterator

while iterator <= 5:
    print '  '*n, # print empty string
    for i in range(start_Number,0,-1): #'for' loop to print the numbers within the range given
        print i,

    for i in range(2,start_Number+1):
        print i,
        
    print    # go to next line if finished printing set of numbers

    n -= 1
    
    start_Number += 1    #increment start_Number to print next set of numbers
    
    iterator += 1              # increment the iterator 
        
